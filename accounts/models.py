from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        # This is a build in attribute (username)
        return "@{}".format(self.username)