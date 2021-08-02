from django.shortcuts import render
from .models import Header, Post

# Create your views here.


def index(request):
    title = Header.objects.all()
    posts = Post.objects.all()

    return render(request, 'index.html', {'title': title, 'posts': posts})

def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'post.html',{'posts':posts})