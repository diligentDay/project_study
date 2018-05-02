from django.template import Library
register=Library()
@register.filter
def mod(num):
    return num%2
@register.filter
def mod2(n1,n2):
    return n1%2
