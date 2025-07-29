from django.db import models
from django import forms
import datetime
from django.utils import timezone

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_text = models.CharField(max_length=200000)
    post_text_field = models.TextField(max_length=200000)
    pub_date = models.DateTimeField("date published")
    post_style = models.CharField(max_length=6)
    post_summary = models.CharField(max_length=20)
    
    def __str__(self):
        return self.post_title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)