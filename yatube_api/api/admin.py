from django.contrib import admin
from posts.models import Post, Group, Comment, Follow

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'pub_date')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created')

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')