from django.db import models
from django.forms import model_to_dict
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


User = get_user_model()


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts', null=True, blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')    
    
    objects = models.Manager() # The default manager.
    tags = TaggableManager()
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    
    @property
    def author_detail(self):
        return model_to_dict(self.author, fields=["username", "first_name", "last_name", "email"])
    
    
    
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, 
                            on_delete=models.CASCADE,
                            related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'