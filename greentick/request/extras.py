from django.db.models import FileField
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.conf import settings

BYTES_IN_MB = 1048576


class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing denied content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            Ex. 2.5MB - 2621440
    """
    def __init__(self, *args, **kwargs):
        # Args or default value
        if 'content_type' in kwargs:
            self.content_types = kwargs.pop('content_types')
        else:
            self.content_types = settings.CONTENT_TYPES

        if 'max_upload_size' in kwargs:
            self.max_upload_size = kwargs.pop('max_upload_size')
        else:
            self.max_upload_size = settings.MAX_UPLOAD_SIZE

        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)

        file = data.file
        content_type = file.content_type
        if file._size > self.max_upload_size:
            raise ValidationError(message='Please keep file size under %(max_upload_size)i Mb.'
                                  'Current file size %(current_file_size)i Mb',
                                  code='invalid_size',
                                  params={'max_upload_size': self.max_upload_size / BYTES_IN_MB,
                                          'current_file_size': file._size / BYTES_IN_MB})

        # Content type blacklist
        if content_type in self.content_types:
            raise ValidationError(message='File extension not supported',
                                  code='invalid_type')

        return data