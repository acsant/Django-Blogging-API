from rest_framework import serializers
from blog.models import BlogEntry
from django.contrib.auth.models import User

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')    
    class Meta:
        model = BlogEntry
        fields = ('id', 'url', 'author', 'title', 'content')
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    blog_entry = serializers.HyperlinkedRelatedField(queryset = BlogEntry.objects.all(), view_name='blog-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'blog_entry')
