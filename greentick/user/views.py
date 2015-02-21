import logging
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from user.models import User as CustomUser, Company
from user.forms import CreateUserForm, LoginForm

logger = logging.getLogger(__name__)


def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/edit.html', {'user': request.user})


def create(request):
    if request.method == 'POST':
        # Form is sent
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Transactional DB Registering
            with transaction.atomic():
                # Get the company
                company, is_company_created = Company.objects.get_or_create(name=form.cleaned_data.get('company'))

                # Create the new user
                custom_user = CustomUser()
                custom_user.user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    form.cleaned_data.get('password'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name')
                )
                custom_user.company = company
                custom_user.job_title = form.cleaned_data.get('job_title')
                custom_user.save()

            logger.info('New user created : %s - %s' % (User, Company))

            # Log the user
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user:
                auth_login(request, user)

            # Redirect on the dashboard
            return redirect('/dashboard/')
    else:
        # Show form
        form = CreateUserForm()

    return render(request, 'user/create.html', {'form': form})


def login(request):
    # Is user already logged ?
    if request.user.is_authenticated():
        return redirect('/dashboard/')

    if request.method == 'POST':
        # Form is sent
        form = LoginForm(request.POST)
        if form.is_valid():
            # Log the user
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user:
                # Authenticate & redirect on the dashboard
                auth_login(request, user)
                return redirect('/dashboard/')
            else:
                messages.add_message(request, messages.INFO, 'Authentication failed')

    else:
        # Show form
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
