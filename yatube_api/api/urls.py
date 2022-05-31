from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


app_name = 'api'


router = DefaultRouter()

router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')
router.register('posts', PostViewSet, basename='post')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
