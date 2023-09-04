from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60, default='Richie Chungus', null=False)
    author_id = models.IntegerField(primary_key=True)
    picture = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png')  

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'picture', 'author_id'],
                name='unique_name_picture_author_id'
            )
        ]
    def natural_key(self):
        return (self.name, self.picture, self.author_id)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=38, primary_key=True)
    timestamp = models.DateTimeField()
    post_text = models.CharField(max_length=300)