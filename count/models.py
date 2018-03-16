from django.db import models
from django.http import HttpResponse
from django.shortcuts import render


class Count(models.Model):
    increment = models.IntegerField(default=0)


class DataStored(models.Model):
    username = models.CharField(max_length=100)
    time = models.TimeField()
    action_type = models.CharField(max_length=100, blank=True)
    count_id = models.ForeignKey(Count)

    def __str__(self):
        return self.username + str(self.time)
