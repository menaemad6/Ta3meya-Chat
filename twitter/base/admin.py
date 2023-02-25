from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount , Trend

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Trend)
admin.site.register(LikePost)
admin.site.register(FollowersCount)