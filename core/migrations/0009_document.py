# Generated by Django 4.2.7 on 2023-11-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('name', models.CharField(blank=True, default='', max_length=250, verbose_name='Name')),
                ('file', models.FileField(blank=True, default='', upload_to='documents/', verbose_name='Document')),
                ('button_text', models.CharField(blank=True, default='', max_length=250, verbose_name='Button Text')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('name',),
            },
        ),
    ]
