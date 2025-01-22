from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter
def get_item(dictionary, key):
    """Returns the value of the dictionary for the given key."""
    return dictionary.get(key)