from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.models import User 


# Create your views here.
def index(request):
    return render(request, "index.html")


