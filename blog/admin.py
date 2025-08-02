from django.contrib import admin
from .models import Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 3  # number of blank upload fields

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]