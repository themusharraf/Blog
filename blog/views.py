from rest_framework.viewsets import ModelViewSet
from blog.models import Post, Comment
from blog.serializers import PostSerializer, PostDetailModelSerializer, CommentModelSerializer
from rest_framework.response import Response
from blog.permissions import IsAuthorOrReadOnly
from rest_framework.generics import ListCreateAPIView


class PostModeViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        self.get_queryset()
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = PostDetailModelSerializer(instance)
        return Response(serializer.data)


class CommentListViewSet(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    permission_classes = [IsAuthorOrReadOnly]
