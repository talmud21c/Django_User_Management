from django.db import models


class ESGData(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=70)
    poi = models.IntegerField()