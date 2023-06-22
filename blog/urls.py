from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostModeViewSet, CommentListViewSet, ProductFavoriteView

router = DefaultRouter()
router.register(r'blog', PostModeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('comment', CommentListViewSet.as_view(), name='comments'),
    path('post/<int:pk>/favorite/', ProductFavoriteView.as_view(), name='product_favorite'),

]
