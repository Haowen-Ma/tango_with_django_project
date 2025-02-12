from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html', takes_context=True)
def get_category_list(context):
    return {'categories': Category.objects.all(),
            'current_category': context.get('category', None)}