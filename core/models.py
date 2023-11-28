from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Updated At')

    class Meta:
        abstract = True  # abstract model means that this model will not be created in database


class GeneralSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=250, blank=True, help_text='Name of the setting')
    description = models.CharField(default='', max_length=250)
    parameters = models.TextField(default='', max_length=750)

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name_plural = 'General Settings'
        verbose_name = 'General Setting'
        ordering = ('name', )


class ImageSetting(AbstractBaseModel):
    name = models.CharField(default='', max_length=250, blank=True, help_text='Name of the setting', verbose_name='Name')
    description = models.CharField(default='', max_length=250, blank=True, verbose_name='Description')
    file = models.ImageField(default='', blank=True, null=True, verbose_name='Image', upload_to='images/')

    def __str__(self):
        return f'Image Setting: {self.name}'

    class Meta:
        verbose_name_plural = 'Image Settings'
        verbose_name = 'Image Setting'
        ordering = ('name', )
