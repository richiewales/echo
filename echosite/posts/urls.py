from django.urls import path
from .views import index, generate_post
urlpatterns = [
    path("", index, name="index"),
    path('generate-post', generate_post, name='generate-post'),
]