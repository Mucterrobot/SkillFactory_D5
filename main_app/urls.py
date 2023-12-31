from django.urls import path

from .views import NewsList, NewsItem, Search, CreatePost, EditPost, DeletePost

urlpatterns = [
  path('', NewsList.as_view()),
  path('<int:pk>', NewsItem.as_view()),
  path('search', Search.as_view()),
  path('add', CreatePost.as_view()),
  path('<int:pk>/edit', EditPost.as_view()),
  path('<int:pk>/delete', DeletePost.as_view()),
]