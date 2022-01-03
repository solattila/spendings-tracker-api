from django.db import models


class Spending(models.Model):
    """
    Spending object.
    """
    created = models.DateTimeField(auto_now_add=True)
    spended_value = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
