from django.urls import path
# from .views import PostListView, PostDetailView
from . import views



urlpatterns = [
    # path('', PostListView.as_view, name='news-home'),
    path('', views.home, name='news-home'),
    # path('news/<pk>/', PostDetailView.as_view(), name='news-detail'),
]
