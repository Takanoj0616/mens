from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TaggedItemBase
import uuid

class UUIDTaggedItem(GenericTaggedItemBase, TaggedItemBase):
    object_id = models.UUIDField(verbose_name='UUID型のオブジェクトID', db_index=True)

class Therapist(models.Model):
    # UUIDをプライマリキーとして設定
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 基本情報
    name = models.CharField(max_length=100, verbose_name="名前")
    age = models.PositiveIntegerField(verbose_name="年齢")
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="身長（cm）")
    bust = models.CharField(max_length=10, verbose_name="バスト")
    waist = models.CharField(max_length=10, verbose_name="ウエスト")
    hip = models.CharField(max_length=10, verbose_name="ヒップ")
    joining_date = models.DateField(verbose_name="入店日")

    # 詳細情報
    comment = models.TextField(verbose_name="コメント", blank=True)
    photo = models.ImageField(upload_to='therapist_photos/', verbose_name="写真", blank=True, null=True)

    
    # 動画情報
    video = models.FileField(upload_to='therapist_videos/', verbose_name="動画", blank=True, null=True)

    # タグ
    tags = TaggableManager(verbose_name='タグ', blank=True, through=UUIDTaggedItem)  # カスタム中間モデルを指定
    
    # NEWタグ用のフィールド
    is_new = models.BooleanField(default=False, verbose_name="NEWタグ")

    # SNS
    x_url = models.URLField(max_length=255, verbose_name='xリンク', blank=True, null=True)
    instagram_url = models.URLField(max_length=255, verbose_name='Instagramリンク', blank=True, null=True)

    # 予約状態
    STATUS_CHOICES = [
        ('available', '予約受付中'),
        ('full', '満員御礼'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name="予約状況"
    )
    class Meta:
        verbose_name = 'セラピスト'
        verbose_name_plural = 'セラピスト一覧'


    # 表示名設定
    def __str__(self):
        return self.name
    
class WorkSchedule(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField(verbose_name="出勤日")

    def __str__(self):
        return f"{self.therapist.name} - {self.date}"