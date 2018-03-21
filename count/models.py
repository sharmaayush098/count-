from django.db import models
from django.http import HttpResponse
from django.shortcuts import render


class Count(models.Model):
    increment = models.IntegerField(default=0)

    def __str__(self):
        return str(self.increment)


class DataStored(models.Model):
    username = models.CharField(max_length=100)
    time = models.TimeField()
    action_type = models.CharField(max_length=100, blank=True)
    count = models.ForeignKey(Count)

    def __str__(self):
        return str(self.count_id) + " " + self.username+" " + self.action_type + " " + str(self.time)
