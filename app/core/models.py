from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
                                        AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionMixin
)
# User = get_user_model
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**kw):
        user=self.model(email=email, **kw)
        user.set_password(password)
        user.save()
        return user
# Create your models here.
class User(AbstractBaseUser,PermissionMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    object = UserManager()
    USERNAME_FIELD = 'email'
