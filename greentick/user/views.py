import logging
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db import transaction
from user.models import User as CustomUser, Company
from user.forms import CreateUserForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index/index.html', {})


def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/edit.html', {'user': request.user})


def create(request):
    if request.method == 'POST':
        # Form is sent
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Get or create the company
            try:
                Company.objects.get(name=form.cleaned_data['company'])
            except Company.DoesNotExist:
                Company(name=form.cleaned_data['company'])

            # Create the new user
            CustomUser.user = User.objects.create_user(
                username,
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            CustomUser.first_name = form.cleaned_data['first_name']
            CustomUser.last_name = form.cleaned_data['last_name']
            CustomUser.company = Company  # @TODO Use get_or_create()
            CustomUser.job_title = form.cleaned_data['job_title']

            # Transactional DB Registering
            with transaction.atomic():
                Company.save()
                CustomUser.save()

            logger.info('New user created : %s - %s' % (User, Company))

            # Log the user
            login(User)

            # Redirect on the dashboard
            return render(request, 'index/index.html', {})
    else:
        # Show form
        form = CreateUserForm()

    return render(request, 'user/create.html', {'form': form})