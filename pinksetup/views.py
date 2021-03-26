from django.template.response import TemplateResponse
from pinksetup.models import PinkSetup, Post
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    return TemplateResponse(request, 'index.html', {'items': PinkSetup.objects.all()})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})


def pinksetup_detail(request, pinksetup_id):
    pinksetup = get_object_or_404(PinkSetup, pk=pinksetup_id)
    return render(request, 'pinksetup_detail.html', {'pinksetup': pinksetup})



