from django.db import models
from django.contrib.auth.models import User

class Youtuber(models.Model):
    youtuber=models.OneToOneField(User,on_delete=models.CASCADE)
    youtubeimage = models.ImageField(upload_to="ChannelPic")
    subscriber = models.ManyToManyField(User,blank=True,related_name="subs")
    channel_name = models.CharField(max_length=100)
# Create your models here.
