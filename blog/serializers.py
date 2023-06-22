from rest_framework.serializers import ModelSerializer
from blog.models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'category', 'title', 'body', 'image')


class PostDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'body', 'view_count', 'image', 'created_at')


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body', 'post', 'owner', 'created_at')
