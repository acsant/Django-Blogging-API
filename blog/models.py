from django.db import models
from django.utils import timezone
# Create your models here.

class BlogEntry(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    author = models.ForeignKey('auth.User', related_name='blog_entry', null=True) 
 
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    
    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(BlogEntry, self).save(*args, **kwargs)        
