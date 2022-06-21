from django.urls import path
from django.views.decorators.cache import cache_page
from home.views import BannerInfoModelView, SingleModelDetailView, WishlistModelListView, add_to_wishlist

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', cache_page(1800)(SingleModelDetailView.as_view()), name='single'),
    path('wishlist/', WishlistModelListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),
    path('', cache_page(10)(BannerInfoModelView.as_view()), name='product'),
]

