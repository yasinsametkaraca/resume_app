from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core.models import AbstractBaseModel


class SkillTypes(AbstractBaseModel):
    name = models.CharField(
        default='',
        max_length=255,
        verbose_name='Name',
        help_text='',
        blank=True,
        null=True,
        unique=True,
    )

    class Meta:
        verbose_name_plural = 'Skill Types'
        verbose_name = 'Skill Type'
        ordering = ('name',)

    def __str__(self):
        return 'Skill Type: %s' % self.name


class Skill(AbstractBaseModel):
    order = models.IntegerField(default=0, verbose_name='Order', help_text='It will be used to sort skills.')
    name = models.CharField(default='', max_length=250, blank=True, help_text='Name of the skill', verbose_name='Name')
    description = models.CharField(default='', max_length=250, blank=True, verbose_name='Description')
    percentage = models.IntegerField(
        default=50,
        blank=True,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )  # Validators are used to validate the data before saving to database. In this case, percentage must be between 0 and 100.
    skill_type = models.ForeignKey(
        SkillTypes,
        default=None,
        on_delete=models.CASCADE,
        verbose_name='Skill Type',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'
        ordering = ('order', )
