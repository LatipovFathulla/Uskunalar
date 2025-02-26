from api.views import BannerInfoModelAPIView, LinesInfoModelAPIView, BiznesInfoModelAPIView, VideoInfoModelAPIView, \
    BlogInfoModelAPIView, AboutInfoModelAPIView, GalleryInfoModelAPIView, WorkInfoModelAPIView, BannerDetailAPIView, \
    LinesDetailAPIView, BiznesDetailAPIView, VideoDetailAPIView, BlogDetailAPIView, AboutDetailAPIView, \
    GalleryDetailAPIView, WorkDetailAPIView, BannerCarouselAPIView, CategoryAPIView, SubCategoryAPIView, \
    PartnersAPIView, LinesCategoriesAPIView, CategoryFilter, SubCategoryFilter, TransModelSerializerAPIView, \
    ALLBannerInfoModelAPIView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('products/', BannerInfoModelAPIView.as_view(), name='products'),
    path('all-products/', ALLBannerInfoModelAPIView.as_view(), name='all-products'),
    path('pr-categories/<int:pk>', CategoryFilter.as_view(), name='pr-categories'),
    path('pr-subcategories/<int:pk>', SubCategoryFilter.as_view(), name='pr-subcategories'),
    path('products/<int:pk>', BannerDetailAPIView.as_view(), name='products-detail'),
    path('lines/', LinesInfoModelAPIView.as_view(), name='lines'),
    path('lines/categories', LinesCategoriesAPIView.as_view(), name='lines'),
    path('lines/<int:pk>', LinesDetailAPIView.as_view(), name='lines-detail'),
    path('biznes/', BiznesInfoModelAPIView.as_view(), name='biznes'),
    path('biznes/<int:pk>', BiznesDetailAPIView.as_view(), name='biznes-detail'),
    path('videos/', VideoInfoModelAPIView.as_view(), name='videos'),
    path('videos/<int:pk>', VideoDetailAPIView.as_view(), name='videos-detail'),
    path('blogs/', BlogInfoModelAPIView.as_view(), name='blogs'),
    path('blogs/<int:pk>', BlogDetailAPIView.as_view(), name='blogs-detail'),
    path('abouts/', AboutInfoModelAPIView.as_view(), name='abouts'),
    path('abouts/<int:pk>', AboutDetailAPIView.as_view(), name='abouts-detail'),
    path('galleries/', GalleryInfoModelAPIView.as_view(), name='galleries'),
    path('galleries/<int:pk>', GalleryDetailAPIView.as_view(), name='galleries-detail'),
    path('works/', WorkInfoModelAPIView.as_view(), name='works'),
    path('works/<int:pk>', WorkDetailAPIView.as_view(), name='works-detail'),
    path('banners/', BannerCarouselAPIView.as_view(), name='banners'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('partners/', PartnersAPIView.as_view(), name='partners'),
    path('sub_categories/', SubCategoryAPIView.as_view(), name='sub_categories'),
    path('trans-banner/', TransModelSerializerAPIView.as_view(), name='trans-banner'),

]