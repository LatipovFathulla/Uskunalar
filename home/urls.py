from django.urls import path

from home.views import BannerInfoModelView, SingleModelDetailView, WishlistModelListView, add_to_wishlist

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', SingleModelDetailView.as_view(), name='single'),
    path('wishlist/', WishlistModelListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>/', add_to_wishlist, name='add-wishlist'),
    path('', BannerInfoModelView.as_view(), name='product'),
]

