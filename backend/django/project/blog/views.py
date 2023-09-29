from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from blog.serializers import UserSerializer, GroupSerializer, BlogPostSerializer, CommentsSerializer, MetaSerializer
from blog.models import BlogPost, Comment, PostMeta


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

class MetaViewSet(viewsets.ModelViewSet):
    queryset = PostMeta.objects.all()
    serializer_class = MetaSerializer