from django.db import models
from django.contrib.auth.models import User

class CreateUpdateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(CreateUpdateModel):
    title = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to='posts', default='posts/default.jpg', max_length=300)
    caption = models.TextField()
    post_type = models.CharField(max_length=10, default='text')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.title

class Comment(CreateUpdateModel):
    text = models.TextField()
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.text + " || " + self.post.title