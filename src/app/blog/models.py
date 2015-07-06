import uuid

from django.contrib.auth.models import User
from django.db import models
    
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(User, related_name='created_events', editable=False, null=True, on_delete=models.SET_NULL, blank=True, verbose_name="Creator")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    title = models.CharField(max_length=144)
    content = models.TextField()
    summary = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name="Tags", blank=True)
    
    def save(self, *args, **kwargs):
        self.summary = self.content[:300]
        super(Post, self).save(*args, **kwargs)