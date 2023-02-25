from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('following', views.following_page, name='following-posts'),
    # path('home', views.home, name='main-page'),
    path('settings', views.settings, name='settings'),
    path('setup-your-account', views.setup, name='setup'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    # path('search-post', views.search_post, name='search-post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('login', views.signin, name='login'),
    path('logout', views.logout, name='logout'),
]