from django import template

register = template.Library()


@register.filter(name='set_class')
def set_class(value, arg):
    return value.as_widget(attrs={'class': arg})
