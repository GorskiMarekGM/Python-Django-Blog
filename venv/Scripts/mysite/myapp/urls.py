from django.urls import path
# . is current directory
from . import views
from . views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView

)

urlpatterns = [

    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
#Create URL pattern that contains a variable
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    
#Create URL pattern for creating new posts
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about"),
]