from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="タイトル")
    description = models.TextField(verbose_name="説明")
    image = models.ImageField(upload_to='topics_images/', verbose_name="画像", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")

    def __str__(self):
        return self.title
    
class Topic2(models.Model):
    title = models.CharField(max_length=200, verbose_name="タイトル")
    description = models.TextField(verbose_name="説明")
    image = models.ImageField(upload_to='topics_images/', verbose_name="画像", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")

    def __str__(self):
        return self.title