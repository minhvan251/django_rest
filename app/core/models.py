# from django.db import models
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import (
#                                         AbstractBaseUser,
#                                         BaseUserManager,
#                                         PermissionMixin
# )
# # User = get_user_model
# class UserManager(BaseUserManager):
#     def create_user(self,email,password=None,**kw):
#         user=self.model(email=email, **kw)
#         user.set_password(password)
#         user.save()
#         return user
# # Create your models here.
# class User(AbstractBaseUser,PermissionMixin):
# 
