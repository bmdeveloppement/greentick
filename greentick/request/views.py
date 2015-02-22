from django.shortcuts import render
from django.contrib import messages
from django.db import transaction
from request.forms import CreateRequestForm

def create(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            # Form is sent
            form = CreateRequestForm(request.POST, request.user)
            if form.is_valid():
                # Transactional DB Registering
                with transaction.atomic():
                    # Create the new request
                    pass

                # Log and notify the user
                logger.info('New request created by %s : %s' % (request.user, 'request_obj'))
                messages.add_message(request, messages.INFO, 'Your request has been created')

                # Redirect on the dashboard
                return redirect('/dashboard/')
        else:
            # Show form
            form = CreateUserForm()

        return render(request, 'user/create.html', {'form': form})
    else:
        messages.add_message(request, messages.INFO, 'You are not connected')
        return render(request, 'index/index.html', {})

