from django.contrib import admin
from blog.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/css/ckeditor5-custom.css',)
        }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)