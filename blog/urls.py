from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(prefix='', viewset=views.PostViewSet)

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<slug:slug>/", views.blog_category, name="blog_category"),
    path("about/", views.about, name="blog_about"),
    path("roadmap/", views.roadmap, name="blog_roadmap"),
    path("projects/", views.projects, name="blog_projects"),
    path("posts/", include(router.urls)) # When using include(), you don't need the name= parameter since the router generates its own names
]