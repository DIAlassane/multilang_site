from django.shortcuts import render
from .models import Post

def ExtendedFront(request):
    posts = Post.objects.all()
    return render(request, 'blog/ExtendedFront.html', {'posts': posts})
