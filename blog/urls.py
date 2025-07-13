from django.urls import path
from . import views


app_name = "blog" # Creating a namespace so I can use the url building stuff
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),
]