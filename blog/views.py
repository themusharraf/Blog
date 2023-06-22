from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from blog.models import Comment
from blog.models import Post
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostDetailModelSerializer
from blog.serializers import PostSerializer, CommentModelSerializer


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


class ProductFavoriteView(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailModelSerializer

    def post(self, request, pk):
        product = self.get_object()
        product.is_favorite = True
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def delete(self, request, pk):
        product = self.get_object()
        product.is_favorite = False
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)
