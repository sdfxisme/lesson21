from django import template

register = template.Library()

def my_upper(string):
    return string.upper()

def my_length(arg):
    return len(arg)

register.filter('my_upper', my_upper)
register.filter('my_length', my_length)