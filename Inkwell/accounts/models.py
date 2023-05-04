from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Username is not provided")
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(username, email, password, **extra_fields)



class CustomUser(AbstractUser):
    # AbstractBaseUser -> password, last_login, is_active
    username = models.CharField(_('username'), max_length=100, unique=False, null=True, default=None)
    email = models.EmailField(_('email address'), unique=True, max_length=254)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
 
    objects = CustomUserManager()

    def __str__(self):
        return str(self.user)

    class Meta:
        swappable = 'AUTH_USER_MODEL'

# class CustomUser(AbstractUser):
#     email = models.EmailField(_('email address'), unique=True, max_length=254)
    
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return str(self.user)

#     class Meta:
#         # Add the username field back to the model
#         swappable = 'AUTH_USER_MODEL'

