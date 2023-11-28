from django import template

register = template.Library()


@register.filter
def get_document_url(file):
    if file:
        try:
            if file.url:
                return file.url
            else:
                raise Exception
        except:
            return ''
    else:
        return ''


@register.filter
def get_object_value_or_none(value):
    if value:
        return value
    else:
        return ''
    