from django.shortcuts import render
from django.utils import timezone
from .models import *
   
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def hots_list(request):
    hots = Hot.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'hots': hots})
def guest_list(request):
    geusts = Guest.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'geusts': geusts})
