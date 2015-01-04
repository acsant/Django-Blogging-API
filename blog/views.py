from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.decorators import list_route
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response
from blog.models import BlogEntry
from blog.permissions import IsOwnerOrReadOnly
from blog.serializers import BlogSerializer, UserSerializer 

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents a blog entry
    """
    queryset = BlogEntry.objects.all()
    serializer_class = BlogSerializer    
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    
    def list(self, request, *args, **kwargs):
        response = super(BlogViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data' : response.data}, template_name = 'blog/blog_entry.html') 
        return response
   
    def retrieve(self, request, *args, **kwargs):
        response = super(BlogViewSet, self).retrieve(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data' : response.data}, template_name = 'blog/blog_detail.html')
        return response    
 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
