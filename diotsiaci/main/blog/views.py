from django.shortcuts import render
from .models import Post
from django.utils.translation import gettext_lazy as _

def ExtendedFront(request):
    posts = Post.objects.all()
    bienvenue_msg = _('Welcome')  
    return render(request, 'blog/ExtendedFront.html', {'posts': posts, 'msg': bienvenue_msg})
