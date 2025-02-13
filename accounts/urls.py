from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('webfeed/', views.webfeed, name='webfeed'),  # Webfeed URL
    path('create_post/', views.create_post, name='create_post'),  # Create post URL
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),  # Like post URL
    # path('home/', views.home, name='home'),
]