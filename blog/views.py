from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    data = Post.objects.all()
    return render(request, 'home.html', {"posts": data})


def post_detail(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {"post": data})
