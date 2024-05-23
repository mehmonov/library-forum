from django.db import models
from user.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to="images/post",verbose_name="Post rasmi", default='image.png')
    
    content = models.TextField(verbose_name="Post uchun matn...")
    
    created = models.DateTimeField(verbose_name='post yaratilgan vaqt', auto_now=True)
    
    def __str__(self) -> str:
        return self.author
    class Meta:
        db_table = 'post'
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
    

    

class Comment(models.Model):
    user =  models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_comment", on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(verbose_name='comment yaratilgan vaqt', auto_now=True)
    def __str__(self) -> str:
        return self.user
    class Meta:
        db_table = 'comment'
        verbose_name = "Comment"
        verbose_name_plural = "Commentlar"
    

    
class Like(models.Model):
    user =  models.ForeignKey(User, related_name="likelar", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_like", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user
    class Meta:
        db_table = 'like'
        verbose_name = "Like"
        verbose_name_plural = "Likelar"
    
