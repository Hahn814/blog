from users.models.profile import UserProfileBase
from django.db import models

class BlogUserProfile(UserProfileBase):
    image = models.ImageField(
        default='profile.jpg',
        upload_to='profile_imgs'
    )