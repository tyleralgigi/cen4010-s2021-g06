from django.db import models
from users.models import User
from uuid import uuid4
import os


def path_and_rename(instance, filename):
    upload_to = 'static/images/'
    ext = filename.split('.')[-1]

    filename = '{}.{}'.format(uuid4(), ext)

    return os.path.join(upload_to, filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    description = models.CharField(max_length=256, null=True)
    image = models.ImageField(upload_to=path_and_rename)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    comment = models.TextField(max_length=256)


class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    report_description = models.TextField(max_length=512, default="")
    timestamp = models.DateTimeField()
