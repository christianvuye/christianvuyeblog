from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = CKEditor5Field('Text', config_name='default')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    page_type = models.CharField(
        max_length=20,
        choices=[
            ('post', 'Regular Post'),
            ('featured', 'Featured Post'),
            ('navbar', 'Navigation Bar Post'),
        ],
        default='post'
    )
    
    def __str__(self):
        return self.title