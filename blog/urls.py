from .views import BlogListview, BlogDetailView
from django.urls import path

urlpatterns = [
    path('', BlogListview.as_view(), name='blog-list-view'),
    path("blog/<int:pk>/",BlogDetailView.as_view(), name= 'blogview'),

]