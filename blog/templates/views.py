from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    #템플릿은 모델명_list.html : post_list.html

class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델명_detail.html : post_list.html