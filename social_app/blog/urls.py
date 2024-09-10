from django.urls import path,include

from . import views
urlpatterns = [
    path('', views.HomeView.as_view(),name='blog-home'),
    path('post/<int:pk>', views.PostDetailsView.as_view(),name='post-detail'), 
    path('post/new/', views.CreatePostView.as_view(),name='create-post'),
    path('post/<int:pk>/update', views.UpdatePostView.as_view(),name='update-post'),    
    path('post/<int:pk>/delete', views.DeletePostView.as_view(),name='delete-post'),    

    path('about/', views.about,name='blog-about'),
]
