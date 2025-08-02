from django.db import models
from django import forms
import datetime
from django.utils import timezone
from markdownx.models import MarkdownxField

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=200000)
    post_text_field = models.TextField(max_length=200000)
    pub_date = models.DateTimeField("date published")
    post_style = models.CharField(max_length=6)
    post_summary = models.CharField(max_length=20)
    post_title = models.CharField(max_length=255)
    post_text_field = MarkdownxField()
    
    def __str__(self):
        return self.post_title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')