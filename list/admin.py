from django.contrib import admin
from .models import Therapist

@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height', 'joining_date', 'x_url', 'instagram_url')  # 一覧表示項目
    search_fields = ('name', 'comment', 'x_url', 'instagram_url')  # 検索対象
    
    # タグ表示メソッド
    def display_tags(self, obj):
        return ','.join(tag.name for tag in obj.tags.all())
    display_tags.short_description = 'タグ'
