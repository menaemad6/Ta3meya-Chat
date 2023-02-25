from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True , null=True)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', blank=True , null=True)
    profilecover = models.ImageField(upload_to='profile_covers',  blank=True , null=True)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True , null=True)
    verified = models.BooleanField(default=False)

    join_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True , null=True)
    image = models.ImageField(upload_to='post_images')
    video = models.FileField(upload_to='tweet_videos' , blank=True , null=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    user_image = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    user_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    


class Trend(models.Model):
    name = models.CharField(max_length=100, blank=True , null=True)
    no_of_tweets = models.IntegerField(default=0)

    def __str__(self):
        return self.name