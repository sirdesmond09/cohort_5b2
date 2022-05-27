from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

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
    
    comments = post.comments.filter(active=True)
    new_comment  = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
        # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    
    data = {'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form}
    
    return render(request, 
                  'blog/post/detail.html',
                  context=data)
    
    
    
def post_share(request, post_id):
     # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
     # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
        # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}\'s comments:\n{cd['comments']}"
            
            # sender = 
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,[cd['to']])
            sent = True

            
    else:
        form = EmailPostForm()
        
    data = {'post': post,
            'form': form,
            "sent":sent}
    
    return render(request, 'blog/post/share.html', context=data)
