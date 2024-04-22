from django.db import models

class PovertyData(models.Model):
    value = models.FloatField()

class InternetData(models.Model):
    value = models.FloatField()

class UnemploymentData(models.Model):
    value = models.FloatField()