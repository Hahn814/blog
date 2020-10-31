from blog.models.posts import PostBase, PostTagBase
from django.db import models
import logging

LOGGER = logging.getLogger(__name__)

class BlogPostTag(PostTagBase):

    def __repr__(self):
        return {
            'tag_name': self.tag_name,
            'tagged_posts': len(self.blogpost_set)
        }

class BlogPost(PostBase):
    tags = models.ManyToManyField(
        to=PostTagBase,
        related_name='tags'
    )

    def __repr__(self):
        return {
            'title': self.title,
            'content_length': len(self.content.split()),
            'author': self.author.get_username(),
            'tags': [repr(tag) for tag in self.tags]
        }
