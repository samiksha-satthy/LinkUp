from django.contrib import admin

from .models import Post, PostAttachment 

admin.site.register(PostAttachment)
admin.site.register(Post)
