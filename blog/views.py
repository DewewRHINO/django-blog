from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.template import loader
from django.http import Http404

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    template = loader.get_template("blog/index.html")
    context = {"latest_post_list": latest_post_list}
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    # try: 
    #     post = Post.objects.get(pk=post_id)
    # except Post.DoesNotExist:
    #     raise Http404("That post does not exist.")
    
    post = get_object_or_404(Post, pk=post_id)
    return render(request,"blog/post.html",{"post":post})