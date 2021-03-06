from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

from django.conf import settings

# class S3CustomStorage(S3BotoStorage):
#     def _normalize_name(self, name):
#         try:
#             return safe_join(self.location, name)
#         except (SuspiciousOperation, ValueError):
#             return ""

class StaticStorage(S3Boto3Storage):

    location = settings.STATICFILES_LOCATION

    def _clean_name(self, name):
        return name

    def _normalize_name(self, name):
        if not name.endswith('/'):
            name += "/"

        name += self.location
        return name


class MediaStorage(S3Boto3Storage):

    location = settings.MEDIAFILES_LOCATION

    def _clean_name(self, name):
        return name

    def _normalize_name(self, name):
        if not name.endswith('/'):
            name += "/"

        name = self.location + name
        return namev

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
