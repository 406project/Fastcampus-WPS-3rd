from django.db import models
from django.conf import settings

__all__ = [
    'Photo',
    'PhotoTag',
    'PhotoComment',
    'PhotoLike',
]


class Photo(models.Model):
    image = models.ImageField(upload_to='photo', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True)
    tags = models.ManyToManyField('PhotoTag')
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PhotoLike',
        related_name='photo_set_like_users'
    )


class PhotoTag(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


class PhotoComment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)