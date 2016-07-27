from django.contrib import admin
from .models import Post , Comment
from treebeard.admin import TreeAdmin

admin.site.register(Post)
@admin.register(Comment)
class CommentAdmin(TreeAdmin):
    pass
# admin.site.register(CommentReply)
# # Register your models here.
