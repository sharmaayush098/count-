from django.db import models


class Count(models.Model):
    increment = models.IntegerField(default=0)



