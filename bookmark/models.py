from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bookmark(models.Model) :
    title = models.CharField('TITLE', max_length=100, blank=True)
    type = models.CharField('TYPE', max_length=100, blank=True, null=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) :
        return self.type