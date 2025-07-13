from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.post_text for q in latest_post_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at Blog %s." % question_id)