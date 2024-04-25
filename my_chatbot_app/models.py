# my_chatbot_app/models.py
from django.db import models
from django.core.validators import MinValueValidator



class PovertyData(models.Model):
    """
    Stores poverty data values, typically fetched from external sources.
    Each record represents the poverty level for a specific date and country.
    """
    value = models.FloatField(validators=[MinValueValidator(0.0)])
    date = models.DateField()
    country = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Poverty Data"
        ordering = ['-date']  # Assuming a 'date' field is added


class InternetData(models.Model):
    value = models.FloatField()

class UnemploymentData(models.Model):
    value = models.FloatField()