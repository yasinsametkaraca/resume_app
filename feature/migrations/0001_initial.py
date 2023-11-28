# Generated by Django 4.2.7 on 2023-11-28 13:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Skill Type',
                'verbose_name_plural': 'Skill Types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('order', models.IntegerField(default=0, help_text='It will be used to sort skills.', verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='Name of the skill', max_length=250, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=250, verbose_name='Description')),
                ('percentage', models.IntegerField(blank=True, default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
                ('skill_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='feature.skilltypes', verbose_name='Skill Type')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ('order',),
            },
        ),
    ]