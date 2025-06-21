from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<slug:slug>/", views.blog_category, name="blog_category"),
    path("about/", views.about, name="blog_about"),
    path("roadmap/", views.roadmap, name="blog_roadmap"),
    path("projects/", views.projects, name="blog_projects"),
]