from django.db import models
from django.db.models import Q

from web.models import Post


class PostManager(models.Manager):

    def active(self):
        return self.filter(status='a')

    def deactive(self):
        return self.filter(status='d')

    def post_contains(self, name):
        return self.filter(
            Q(title__icontains=name) |
            Q(description__icontains=name)
        ).exclude(status='active')
