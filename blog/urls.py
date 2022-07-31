from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('post_detail/<slug:slug>', views.post_detail, name="post_detail"),
]
