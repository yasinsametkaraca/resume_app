from django.db import models


class GeneralSettings(models.Model):
    name = models.CharField(default='', max_length=250, blank=True)
    description = models.TextField(default='', max_length=250)
    parameters = models.TextField(default='', max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
