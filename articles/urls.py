from django.urls import path
from .views import ArticleListCreate, ArticleDetail

urlpatterns = [
    path('article/', ArticleListCreate.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
]