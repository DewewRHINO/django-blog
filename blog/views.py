from django.shortcuts import render,get_object_or_404
import markdown # For ToC
# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.template import loader
from django.http import Http404
from django.views import generic

md_extensions = ['extra', 'toc']

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Render Markdown with ToC
        post_body = self.object.post_text_field
        md = markdown.Markdown(extensions=['extra', 'toc'])
        post_html = md.convert(post_body)
        toc_html = md.toc

        # Add both to context
        context['post_html'] = post_html
        context['toc_html'] = toc_html
        return context