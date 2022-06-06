from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField(read_only=True)
    author_detail = serializers.ReadOnlyField()
    
    class Meta:
        model = Post
        fields = '__all__'
        # write_only_fields = ["author"]
        