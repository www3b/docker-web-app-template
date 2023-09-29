from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import BlogPost, Comment, Tag, PostMeta


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'created_at', 'cover', 'tags', 'meta']
        
class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['blog_post', 'text', 'author', 'meta']
        
class MetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostMeta
        fields = ['likes', 'views']