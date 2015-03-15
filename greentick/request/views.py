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
                import pdb; pdb.set_trace()
                for uploaded_file in request.FILES:
                    file_obj = File()
                    file_obj.user = user_obj
                    file_obj.request = request_obj
                    file_obj.name = uploaded_file.name
                    file_obj.type = uploaded_file.content_type
                    file_obj.size = uploaded_file._size
                    file_obj.file = uploaded_file
                    file_obj.full_clean()
                    file_obj.save()
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
