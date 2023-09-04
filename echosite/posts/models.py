from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    author_id = models.IntegerField(primary_key=True)
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=38, primary_key=True)
    timestamp = models.DateTimeField()
    post_text = models.CharField(max_length=300)
