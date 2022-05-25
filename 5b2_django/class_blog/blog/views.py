from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.published.all()
    data = {'posts': posts}
    
    return render(request,'blog/post/list.html', context=data)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                              slug=post,
                              status='published',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    
    data = {'post': post}
    return render(request, 
                  'blog/post/detail.html',
                  context=data)