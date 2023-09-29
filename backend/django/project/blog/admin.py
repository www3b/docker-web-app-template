from django.contrib import admin
from .models import BlogPost, Comment, PostMeta, Tag
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(PostMeta)
admin.site.register(Tag)