from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog" # Creating a namespace so I can use the url building stuff
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)