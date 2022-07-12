
from django.contrib.auth.models import BaseUserManager
from django.db import models
from accounts.sender import send_otp
from painless.models.querysets import OTPRequestQuerySet


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mobile_number, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not mobile_number:
            raise ValueError('The given email must be set')
        mobile_number = self.normalize_email(mobile_number)
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, mobile_number, password=None, **extra_fields):
        """Create and save a regular User with the given emmobile_numberail and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_number, password, **extra_fields)
    

    def create_superuser(self, mobile_number, password, **extra_fields):
        """Create and save a SuperUser with the given mobile_number and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            

        return self._create_user(mobile_number, password, **extra_fields)






class OTPManager(models.Manager):
    def get_queryset(self):
        return OTPRequestQuerySet(self.model, self._db)

    def is_valid(self, receiver, code):
        return self.get_queryset().is_valid(receiver, code)


    def generate(self, data):
        otp = self.model(channel = data['channel'], receiver=data['receiver'])
        otp.save(using = self._db)
        send_otp(otp)
        return otp