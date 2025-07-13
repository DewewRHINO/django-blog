from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.template import loader

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    template = loader.get_template("blog/index.html")
    context = {"latest_post_list": latest_post_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at Blog %s." % question_id)