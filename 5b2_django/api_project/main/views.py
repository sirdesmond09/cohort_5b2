from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from rest_framework.exceptions import NotFound
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from account.permissions import IsAuthorOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

class BlogPostList(APIView):
    """
    List all blog posts, or create a new post.
    """
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request, format=None):
        # user = request.user #get all the users
        # blog_posts = user.blog_posts.filter(status="published") #get all publihsed post for loggedin user
        blog_posts = Post.objects.filter(status="published")
        serializer = PostSerializer(blog_posts, many=True) #serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BlogPostDetail(APIView):
    """
    Retrieve, update or delete a blog post instance.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthorOrReadOnly]
    
    def get_object(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            raise NotFound(detail={"message":"The data does not exist"}, code=status.HTTP_404_NOT_FOUND)

    def get(self, request, post_id, format=None):
        blog_post = self.get_object(post_id)
        serializer = PostSerializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(methods=['put'], request_body = PostSerializer())
    @action(methods=['put'], detail=True)
    def put(self, request, post_id, format=None):
        blog_post = self.get_object(post_id)
        self.check_object_permissions(request, blog_post)
        serializer = PostSerializer(blog_post, data=request.data, partial=True)
        if serializer.is_valid():
            print(serializer.partial)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, format=None):
        blog_post = self.get_object(post_id)
        self.check_object_permissions(request, blog_post)
        blog_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)