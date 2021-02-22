from django.test import TestCase
from blog.models import BlogPost, BlogPostTag

from django.utils import timezone
from django.contrib.auth.models import User


class BlogPostTestCase(TestCase):
    test_user = User.objects.create(username='Test User')
    test_time = timezone.now()

    def test_post(self):
        post = BlogPost(
            title='Test Post',
            content='<h1>Test Post</h1>',
            author=BlogPostTestCase.test_user,
            date_posted=BlogPostTestCase.test_time
        )

        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.content, "<h1>Test Post</h1>")
        self.assertEqual(post.author, BlogPostTestCase.test_user)
        self.assertEqual(post.date_posted, BlogPostTestCase.test_time)
