# Generated by Django 4.2.7 on 2023-11-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(help_text='Name of the message', max_length=250, verbose_name='Name')),
                ('email', models.EmailField(help_text='Email of the message', max_length=250, verbose_name='Email')),
                ('subject', models.CharField(help_text='Subject of the message', max_length=250, verbose_name='Subject')),
                ('message', models.TextField(help_text='Message', verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('name',),
            },
        ),
    ]
