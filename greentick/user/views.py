from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth import login
from user.models import User
from user.forms import CreateUserForm


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
            # Create the new user
            new_user = User.objects.create_user(
                self.cleaned_data['username'],
                self.cleaned_data['email'],
                self.cleaned_data['password']
            )
            new_user.first_name = self.cleaned_data['first_name']
            new_user.last_name = self.cleaned_data['last_name']
            new_user.company = self.cleaned_data['company']
            new_user.job_title = self.cleaned_data['job_title']
            new_user.save()

            # Log the user
            login(new_user)

            # Redirect on the dashboard
            return render(request, 'index/index.html', {})
    else:
        # Show form
        form = CreateUserForm()

    return render(request, 'user/create.html', {'form': form})