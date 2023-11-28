from django.conf import settings
from core.models import ImageSetting


def get_image(setting):
    try:
        image = ImageSetting.objects.get(name=setting).file.url
        if not image:
            raise Exception
    except:
        image = settings.DEFAULT_PNG

    return image