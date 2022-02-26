from django import template

register = template.Library()


@register.simple_tag
def get_url_lang(request, lang):
    url = request.path.split('/')
    url[1] = lang
    return '/'.join(url)


@register.simple_tag
def get_wishlist_count(request):
    wishlist = request.session.get('wishlist')
    if wishlist:
        return len(wishlist)
    return 0


@register.simple_tag
def get_price(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'