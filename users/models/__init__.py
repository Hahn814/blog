from users.models.profile import UserProfileBase
from blog.models import BlogPost
from django.db import models

class BlogUserProfile(UserProfileBase):
    image = models.ImageField(
        default='default.jpg',
        upload_to='profile_pics'
    )

    def get_posts(self):
        return BlogPost.objects.filter(author=self.user)