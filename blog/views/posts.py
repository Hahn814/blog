from django.urls import reverse
from django.views.generic import DetailView
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils import timezone


from blog.models import BlogPost
import logging

LOGGER = logging.getLogger(__name__)


class PostView(DetailView):

    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
