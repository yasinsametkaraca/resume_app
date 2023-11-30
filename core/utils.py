from django.conf import settings
from core.models import ImageSetting


def get_val_in_type(value, val_type):
    try:
        if val_type == 'str':
            value = str(value)
        elif val_type == 'int':
            value = int(value)
        elif val_type == 'float':
            value = float(value)
        elif val_type == 'bool':
            if str(value).lower() == 'true':
                value = True
            elif str(value).lower() == 'false':
                value = False
            elif str(value).lower() == 'none':
                value = None
            else:
                value = None
    except:
        value = None

    return value


def get_image(setting):
    try:
        image = ImageSetting.objects.get(name=setting).file.url
        if not image:
            raise Exception
    except:
        image = settings.DEFAULT_PNG

    return image


def get_general_setting_parameter(setting_name, val_type='str'):
    from core.models import GeneralSetting
    try:
        parameter = GeneralSetting.objects.get(name=setting_name).parameter
    except:
        parameter = ''
    parameter = get_val_in_type(parameter, val_type)

    return parameter


def delete_media_file(model, instance=None, delete_older=False, path=None):
    """
    Delete old file from media storage when new file is uploaded.
    If path is not None, delete file from path. If path is None, delete file from media storage and instance must be given.
    :param model: Django Model to connect related database row.
    :param instance: Instance of model that is currently uploaded.
    :param delete_older: If True, delete old file from media storage; if False, delete current object's file.
    :param path: Path of file. Optional.
    :return True if file is deleted, False if file is not deleted.:
    """

    if path:
        old_file_path = path
    else:
        if not instance:
            return False
        if delete_older:
            # This is for updating instance process.
            # Delete older file that is on the instance.
            if not instance.pk:
                # Given instance is not saved yet. So there is no older file.
                return False

            try:
                instance_object = model.objects.get(pk=instance.pk)
            except model.DoesNotExist:
                # Given instance could not be found in database.
                return False
            new_file = instance.file
            try:
                new_file.file  # This will raise FileDoesNotExist if file is cleared from instance, which is file deletion request.
                if new_file._committed:
                    # New file is already uploaded.
                    # That case only possible when updating instance without changing file, which means old_file=new_file.
                    # Since they are equal, it must not be deleted. There is no actually new file.
                    old_file = None
                else:
                    # New file is not uploaded yet which means there is old file.
                    old_file = instance_object.file
            except:
                old_file = instance_object.file
        else:
            # Delete current file
            old_file = instance.file

        if old_file:
            old_file_path = old_file.name
        else:
            old_file_path = None

    if old_file_path:
        if instance.file.storage.exists(old_file_path):
            instance.file.storage.delete(old_file_path)
            return True

    return False