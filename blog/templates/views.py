
from django.views.generic import ListView, DetailView

from .models import Post


# def index(request):
#     posts = Post.object.all().order_by('-pk')
#     return render(request, 'blog/index.html', {'posts':posts})
#
# def single_post_page(request,pk):
#     post1 = Post.objects.get(pk=pk)
#     return render(request, 'blog.single_post_page.html', {'post':post1})


class PostList(ListView):
    model = Post
    ordering = '-pk'
    #템플릿은 모델명_list.html : post_list.html

class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델명_detail.html : post_list.html