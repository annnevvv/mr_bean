from django import template

from image_app.models import ImageModel

register = template.Library()


@register.simple_tag
def total_img(user):
    counter = ImageModel.objects.filter(user=user).count()
    print(counter)
    return counter


@register.filter(name='enumerate_list')
def enumerate_list(value):
    return enumerate(value, 1)
