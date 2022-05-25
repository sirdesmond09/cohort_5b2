from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 2) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    data = {'posts': posts,
            'page': page,}
    
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