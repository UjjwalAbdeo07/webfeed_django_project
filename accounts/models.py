from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of post creation

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who liked the post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Post that was liked
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the like

    def __str__(self):
        return f"Like by {self.user.username} on {self.post.id}"
    
