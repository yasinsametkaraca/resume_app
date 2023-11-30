from django.dispatch import receiver
from django.db import models, IntegrityError

from core.utils import delete_media_file
from models import ImageSetting, Document


@receiver(models.signals.post_delete, sender=ImageSetting)
@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    delete_media_file(sender, instance=instance, delete_older=False)


@receiver(models.signals.pre_save, sender=ImageSetting)
@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    delete_media_file(sender, instance=instance, delete_older=True)