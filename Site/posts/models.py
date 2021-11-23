from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Post(models.Model):
    post_title = models.CharField(max_length=60, help_text="Enter title (60 characters max)", blank=True)
    image = models.ImageField(upload_to='', blank=True)
    post_text = models.CharField(max_length=400, help_text="Write your post...")
    post_author = models.ForeignKey(User, on_delete= models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
