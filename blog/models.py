from django.db import models
from django.utils import timezone
from treebeard.al_tree import AL_Node

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(AL_Node):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               db_index=True,
                               blank=True,)
    sib_order = models.PositiveIntegerField(default=0)
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


# class CommentReply(models.Model):
#     comment = models.ForeignKey('blog.Comment',related_name='replies')
#     reply_author = models.ForeignKey('auth.User')
#     reply_text = models.TextField(max_length=350)
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
#
#
#     def approve(self):
#         self.approved_comment = True
#         self.save()
#
#     def __str__(self):
#         return self.reply_text
