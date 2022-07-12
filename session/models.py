
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from painless.models.choices import  UserTypeChoices
from painless.models.mixins import TimeStampedMixin
User = get_user_model()



class Session(TimeStampedMixin):
    uid = models.UUIDField(_('uid'),primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True, related_name="session")
    user_type = models.CharField(_('user_type'),max_length = 225, choices = UserTypeChoices.choices, default = UserTypeChoices.USER)
    device_name = models.CharField('device',max_length = 225, blank = True, null = True)
    notification_token = models.CharField(_('notification_token'), max_length = 128, null = True, blank = True)
    uniqe_device_code = models.CharField(_('uniqe_device'), null = True, blank = True, max_length= 128)
    client_version = models.CharField(_('client_version'), max_length = 20, blank = True, null = True)
    server_version = models.CharField(_('server_version'), max_length = 100, blank = True, null = True)
    refresh_has_token = models.CharField(_('refresh_token'), blank = True, null = True, max_length=225)
    client_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("remote address"))
    is_blooked  = models.BooleanField(blank = True, null = True)


    class Meta:
        verbose_name = _('session')
        verbose_name_plural = _('sessions')
    
    def __str__(self) -> str:
        return "{}".format(self.client_ip)



