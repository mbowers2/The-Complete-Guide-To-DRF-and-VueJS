from django.urls import path

from news.api.views import article_list_create_api_view, \
    article_detail_api_view, ArticleListCreateAPIView, ArticleDetailAPIView, \
    JournalistListCreateAPIView

urlpatterns = [
    path('articles/', article_list_create_api_view, name='article_list'),
    path('articles/<int:pk>', article_detail_api_view, name='article_detail'),
    path('articles/class/', ArticleListCreateAPIView.as_view(), name='article_list_class'),
    path('articles/class/<int:pk>', ArticleDetailAPIView.as_view(), name='article_detail_class'),
    path('journalists/class/', JournalistListCreateAPIView.as_view(), name='journalist_list_class'),
]

