import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from request.forms import CreateRequestForm, UploadFileForm
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

            # Log and notify the user
            logger.info('New request created by %s : %s' % (request.user, request_obj.id))
            messages.add_message(request,
                                 messages.INFO,
                                 'Your request has been created. Drop here some files if needed.')

            # Redirect on the dashboard
            return redirect('/request/upload-file/%i' % request_obj.id)

    return render(request, 'request/create.html', {'form': form})


def upload_file(request, request_id):
    # Check authentication
    if not request.user.is_authenticated():
        messages.add_message(request, messages.INFO, 'You are not connected')
        return render(request, 'index/index.html', {})

    # Get user and form
    user_obj = User.objects.filter(pk=request.user.id).get()
    request_obj = Request.objects.filter(pk=request_id).get()

    form = UploadFileForm(request.POST or None)

    # Process form
    if form.is_valid():
        try:
            for key in request.FILES:
                # Save file and properties
                file = request.FILES[key]
                file_obj = File()
                file_obj.user = user_obj
                file_obj.request = request_obj
                file_obj.name = file.name
                file_obj.type = file.content_type
                file_obj.size = file._size
                file_obj.file = file
                file_obj.full_clean()
                file_obj.save()
            return HttpResponse(status=201)
        except Exception as e:
            message = 'An error occured while uploading the file'
            if e.message_dict['file']:
                # Specific error
                message = e.message_dict['file']
            return HttpResponse(message, status=403)

    return render(request, 'request/upload-file.html', {'form': form, 'request': request_obj})