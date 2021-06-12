from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.CharField(max_length=50, null=True)
    blog = models.TextField(null=True)
    coverimage = models.ImageField(upload_to="cover_image/blogs", null=True)