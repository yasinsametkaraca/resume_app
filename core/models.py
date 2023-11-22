from django.db import models


class GeneralSetting(models.Model):
    name = models.CharField(default='', max_length=250, blank=True, help_text='Name of the setting')
    description = models.CharField(default='', max_length=250)
    parameters = models.TextField(default='', max_length=750)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name_plural = 'General Settings'
        verbose_name = 'General Setting'
        ordering = ('name', )
