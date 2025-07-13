from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.template import loader
from django.http import Http404
from django.views import generic

class IndexView(generic.ListView):
    context_object_name = "latest_post_list"
    # latest_post_list = Post.objects.order_by("-pub_date")[:5]
    template_name = "blog/index.html"
    # context = {"latest_post_list": latest_post_list}
    
    def get_queryset(self): 
        return Post.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/post.html"