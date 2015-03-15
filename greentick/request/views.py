import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.core.exceptions import ValidationError
from request.forms import CreateRequestForm
from user.models import User
from request.models import Request, Type, File


logger = logging.getLogger(__name__)


def create(request):
    # Check authentication
    if not request.user.is_authenticated():
        messages.add_message(request, messages.INFO, 'You are not connected')
        return render(request, 'index/index.html', {})

    # Get user and form
    user_obj = User.objects.filter(pk=request.user.id).get()
    form = CreateRequestForm(request.POST or None, user=user_obj)

    # Process form
    if form.is_valid():
        # Transactional DB Registering
        try:
            with transaction.atomic():
                # Get type obj
                type_obj = form.cleaned_data.get('type')

                # Create the new request
                request_obj = Request()
                request_obj.user = user_obj
                request_obj.type = type_obj
                request_obj.name = form.cleaned_data.get('name')
                request_obj.description = form.cleaned_data.get('description')
                request_obj.tracking_reference = form.cleaned_data.get('tracking_reference')
                request_obj.save()

                # Upload files
                # import pdb; pdb.set_trace()
                for key in request.FILES:
                    handle_uploaded_file(user_obj, request_obj, request.FILES[key])

        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
            return render(request, 'request/create.html', {'form': form})

        # Log and notify the user
        logger.info('New request created by %s : %s' % (request.user, request_obj.id))
        messages.add_message(request, messages.INFO, 'Your request has been created. Notifications has been sent to %s' %
                             'bm@gmail.com')

        # Redirect on the dashboard
        return redirect('/dashboard/')

    return render(request, 'request/create.html', {'form': form})


def handle_uploaded_file(user, request, file):
    # Save file and properties
    file_obj = File()
    file_obj.user = user
    file_obj.request = request
    file_obj.name = file.name
    file_obj.type = file.content_type
    file_obj.size = file._size
    file_obj.file = file
    file_obj.full_clean()
    return file_obj.save()