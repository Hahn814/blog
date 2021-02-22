# -*- coding: utf-8 -*-

"""
Blog post models
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

import logging

LOGGER = logging.getLogger(__name__)


class PostTagBase(models.Model):
    tag_name = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.tag_name

    def __repr__(self):
        return {
            'tag_name': self.tag_name
        }


class PostBase(models.Model):
    title = models.CharField(
        max_length=100
    )
    content = HTMLField()
    date_posted = models.DateTimeField(
        default=timezone.now
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def __repr__(self):
        return {
            'title': self.title,
            'content_length': len(self.content.split()),
            'author': self.author.get_username(),
        }