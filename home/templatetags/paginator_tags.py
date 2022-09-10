from django import template
from django.core.paginator import Paginator

from home.models import ProductSpecificationsModel, CategoryModel, SubCategoryModel

register = template.Library()


@register.simple_tag
def get_proper_elided_page_range(p, number, on_each_side=3, on_ends=2):
    paginator = Paginator(p.object_list, p.per_page)
    return paginator.get_elided_page_range(number=number,
                                           on_each_side=on_each_side,
                                           on_ends=on_ends)


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url


@register.simple_tag()
def delete_duplicate():
    return ProductSpecificationsModel.objects.values_list('product_id', flat=True).order_by('pk').distinct('product_id')


@register.filter
def get_category_name(categories, category_id):
    try:
        return categories.get(id=category_id)
    except CategoryModel.DoesNotExist:
        pass


@register.filter
def get_subcategory_name(subcategories, subcategory_id):
    try:
        return subcategories.get(id=subcategory_id)
    except SubCategoryModel.DoesNotExist:
        pass

