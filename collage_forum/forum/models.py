from django.db import models

from django.contrib.auth.models import User

class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='comment_images/', null=True, blank=True)  # Optional image upload
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.forum.title}"
