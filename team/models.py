from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=400)
    Description = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.Description[:100] + '....'
