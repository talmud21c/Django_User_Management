from django.db import models
from django.conf import settings


class ESGData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=70)
    poi = models.IntegerField()