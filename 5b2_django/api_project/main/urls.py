from django.urls import path
from . import views

urlpatterns = [ 
    path("posts/", views.BlogPostList.as_view()),
    path("posts/<int:post_id>/", views.BlogPostDetail.as_view()),  
]