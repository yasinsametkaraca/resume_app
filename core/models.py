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


class Document(AbstractBaseModel):  # This model is used to store documents. For example, CV. Slug means the last part of the URL. For example, "https://www.example.com/blog/this-is-a-slug". In this case, "this-is-a-slug" is the slug.
    slug = models.SlugField(default='', max_length=250, blank=True, help_text='Slug of the document', verbose_name='Slug')  # SlugField is used to store slugs. Slugs are used to create SEO friendly URLs.
    file = models.FileField(default='', blank=True, verbose_name='Document', upload_to='documents/')  # This field is used to store the file of the document. For example, "CV.pdf".
    button_text = models.CharField(default='', max_length=250, blank=True, verbose_name='Button Text')  # This field is used to store the text of the button. For example, "Download CV".
    show_on_page = models.BooleanField(default=True, verbose_name='Show On Menu')  # This field is used to determine whether to show the document on the page or not.

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name_plural = 'Documents'
        verbose_name = 'Document'
        ordering = ('slug', )
