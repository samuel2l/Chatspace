from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.HomeView.as_view(),name='blog-home'),
    path('post/<int:pk>', views.PostDetailsView.as_view(),name='post-detail'), 
    path('post/new/', views.CreatePostView.as_view(),name='create-post'),    
    path('about/', views.about,name='blog-about'),
]
