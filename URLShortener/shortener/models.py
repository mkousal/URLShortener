from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class URL(models.Model):
    long_url = models.URLField(max_length=2048)
    short_url = models.CharField(unique=True, max_length=7, primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    clicks = models.IntegerField(default=0)

    class Meta:
        app_label = 'shortener'

    def __str__(self):
        return "%s" % (self.pk)