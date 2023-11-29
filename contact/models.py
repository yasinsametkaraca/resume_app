from django.db import models
from core.models import AbstractBaseModel


class Message(AbstractBaseModel):  # This model is used to store messages from the contact form.
    name = models.CharField(max_length=250, blank=False, null=False, help_text='Name of the message', verbose_name='Name')
    email = models.EmailField(max_length=250, blank=False, null=False, help_text='Email of the message', verbose_name='Email')
    subject = models.CharField(max_length=250, blank=False, null=False, help_text='Subject of the message', verbose_name='Subject')
    message = models.TextField(blank=False, help_text='Message', null=False, verbose_name='Message')

    def __str__(self):
        return f'Message: {self.name}'

    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Message'
        ordering = ('name', )


