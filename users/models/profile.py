from django.db import models
from django.contrib.auth.models import User

class UserProfileBase(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )

    @property
    def name(self):
        return self.user.get_full_name()

    @property
    def username(self):
        return self.user.get_username()
    
    def __str__(self):
        return "{username} UserProfile".format(username=self.user.get_username())

    def __repr__(self):
        return {
            'username': self.user.get_username(),
            'name': self.user.get_full_name(),
            'superuser': self.user.is_superuser,
            'active': self.user.is_active,
            'staff': self.user.is_staff,
            'id': self.user.id
        }