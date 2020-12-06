from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def blogHome(request):
    return render(request, 'blog/blogHome.html')

def blogPost(request, slug):
    return render(request, 'blog/blogPost.html')