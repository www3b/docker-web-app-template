from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class PostMeta(models.Model):
  likes = models.IntegerField(default=0, editable=False)
  views = models.IntegerField(default=0, editable=False)
  
  
class BlogPost(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=300)
  text = models.TextField()
  cover = models.ImageField(upload_to='uploads/img/%Y/%m/%d')
  created_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  tags = models.ManyToManyField("Tag")  
  # meta = models.ForeignKey("PostMeta", on_delete=models.CASCADE, editable=False, default=PostMeta())
  test = models.IntegerField(default=0, editable=False)



class Comment(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
  text = models.TextField()
  author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  meta = models.ForeignKey("PostMeta", on_delete=models.CASCADE)
  
  
class Tag(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100)
  def __str__(self):
      return self.name
  
  
  