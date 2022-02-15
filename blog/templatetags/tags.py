from django import template

register = template.Library()


@register.simple_tag
def get_wishlist_count(request):
    wishlist = request.session.get('wishlist')
    if wishlist:
        return len(wishlist)
    return 0