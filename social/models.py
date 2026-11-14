from django.conf import settings
from django.db import models
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="profile")
    bio=models.CharField(max_length=250,blank=True)
    avatar=models.ImageField(upload_to="avatars/",blank=True,null=True)
    def __str__(self): return f"{self.user.username}'s profile"
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="posts")
    caption=models.TextField(max_length=2000)
    image=models.ImageField(upload_to="posts/",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["-created_at"]
    def __str__(self): return f"Post by {self.author.username}"
class Like(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="likes")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: constraints=[models.UniqueConstraint(fields=["user","post"],name="unique_user_post_like")]
class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="comments")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    body=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=["created_at"]
class Follow(models.Model):
    follower=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="following")
    followed=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="followers")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints=[models.UniqueConstraint(fields=["follower","followed"],name="unique_follow")]
        ordering=["-created_at"]
