from django.contrib import admin
from blog.models import Category, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmion(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmion)
admin.site.register(Comment, CommentAdmin)