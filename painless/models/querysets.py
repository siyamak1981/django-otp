from django.db import models
from datetime import  timedelta
from django.utils import timezone




class PostStatusQuerySet(models.QuerySet):
    def drafts(self):
        return self.filter(status = 0)

    def published(self):
        return self.filter(status = 1)


class OTPRequestQuerySet(models.QuerySet):
    def is_valid(self, receiver, code):
        current_time = timezone.now()
        return self.filter(
            # request_id = request,
            receiver = receiver,
            code = code,
            created__lte = current_time,
            created__gt = current_time-timedelta(seconds = 128), # its valid in duration 128 seconds
         ).exists()
