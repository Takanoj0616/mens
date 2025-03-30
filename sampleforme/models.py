from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'サンプル投稿'
        verbose_name_plural = '投稿内容'

    def __str__(self):
        return self.title

