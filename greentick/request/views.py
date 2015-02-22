import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from request.forms import CreateRequestForm
from user.models import User

logger = logging.getLogger(__name__)


def create(request):
    if request.user.is_authenticated():
        # Get the full user obj from SimpleLazyLoad user obj
        user = User.objects.filter(pk=request.user.id).get()
        if request.method == 'POST':
            # Form is sent
            form = CreateRequestForm(request.POST, user=user)
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
            form = CreateRequestForm(user=user)

        return render(request, 'user/create.html', {'form': form})
    else:
        messages.add_message(request, messages.INFO, 'You are not connected')
        return render(request, 'index/index.html', {})
