import uuid
import string
from random import SystemRandom
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from painless.models.managers import OTPManager, UserManager
from painless.models.validations import validate_phone_number
from painless.models.mixins import TimeStampedMixin
from painless.models.choices import GenderChoices, OTPCHannel, ValidationChoices
from django.templatetags.static import static




class City(TimeStampedMixin):
    title = models.CharField(_('title'),max_length = 64, unique = True, null = True, blank = True)
    province = models.ForeignKey('Province', on_delete = models.CASCADE, related_name='provice')

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.title


class Province(TimeStampedMixin):
    title = models.CharField(_('title'),max_length = 64, null = True, blank = True)

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

    def __str__(self):
        return self.title


class User(AbstractUser,TimeStampedMixin):
    username = None
    published_at = None
    mobile_number = models.CharField(_('mobile'), max_length = 12, validators=[validate_phone_number])
    
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []


    objects = UserManager()

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
    
    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email





class Profile(TimeStampedMixin):

    user = models.OneToOneField('User', related_name="profile", on_delete=models.CASCADE ,verbose_name = _('User'))
    avatar = models.ImageField(_('image'), upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    varification_type = models.CharField(_('varification_type'), max_length = 225, choices=ValidationChoices.choices, null=True, blank=True, default = ValidationChoices.MOBILE)
    gender = models.CharField(_('gender'), max_length = 225, choices=GenderChoices.choices, null=True, blank=True, default = GenderChoices.MALE)
    job = models.CharField(_('job'), max_length=128, blank = True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null = True, blank = True)
    address = models.CharField(_('address'), max_length=228, blank = True, null = True)
    birth_date = models.DateField(_('birthdate'), null=True, blank=True)
    level = models.IntegerField(_('level'), blank = True, null = True)


    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('')

    def __str__(self):
        return f'({self.city})'






def generate_otp():
    rand = SystemRandom()
    digits = rand.choices(string.digits, k = 4)
    return "".join(digits)


class SendSmsRequest(models.Model):

    request_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    channel = models.CharField(_('channel'),max_length = 225, blank = True, null = True, choices=OTPCHannel.choices, default=OTPCHannel.PHONE)
    receiver = models.CharField(_('receiver'),max_length=12, blank = True, null =True,validators=[validate_phone_number])
    code = models.CharField(_('code'),max_length=225, default = generate_otp, blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    sendsms = models.ForeignKey('User', on_delete = models.CASCADE, blank = True, null = True, related_name="sendsms")

    objects = OTPManager()

    class Meta:
        verbose_name = _('sendsms')
        verbose_name_plural = _('sendsms')





