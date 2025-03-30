from django.db import models
from list.models import Therapist

class Review(models.Model):
    girl = models.ForeignKey(
        Therapist,
        on_delete=models.CASCADE,
        verbose_name='女の子'
    )
    customer_name = models.CharField(
        max_length=100,
        verbose_name='お客様のお名前'
    )
    visit_date = models.DateField(
        verbose_name='ご来店日'
    )
    comment = models.TextField(
        verbose_name='コメント'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = '口コミ'
        verbose_name_plural = '口コミ一覧'

    def __str__(self):
        return f'{self.customer_name} - {self.girl.name}'