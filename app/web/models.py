import uuid
from enum import Enum

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):

    _id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Post(BaseModel):

    class PostStatus(Enum):
        ACTIVE = ('a', 'active')
        DEACTIVE = ('d', 'deactive')
        UNKNOWN = ('u', 'unknown')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]


    title = models.CharField(max_length=255)
    slug = models.SlugField(default='', null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='media/Post/thumbnail/')
    status = models.CharField(max_length=1, choices=[x.value for x in PostStatus])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
