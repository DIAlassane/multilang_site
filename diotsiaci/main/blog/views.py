from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from django.utils.translation import activate

def switch_to_french(request):
    activate('fr')
    return redirect('/')

def switch_to_english(request):
    activate('en')
    return redirect('/')


def ExtendedFront(request):
    posts = Post.objects.all()
    return render(request, 'blog/ExtendedFront.html', {'posts': posts})
