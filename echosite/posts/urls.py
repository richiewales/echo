from django.urls import path
from .views import index, generate_post, consume_posts, get_posts
urlpatterns = [
    path("", index, name="index"),
    path('generate-post', generate_post, name='generate-post'),
    path('consume-posts', consume_posts, name='consume-posts'),
    path('get-posts', get_posts, name='get-posts')
]