from django.contrib import admin
from .models import Therapist, WorkSchedule

# 出勤予定のインライン設定
class WorkScheduleInline(admin.TabularInline):
    model = WorkSchedule
    extra = 1  # 最初に表示する空の行数
    verbose_name = "出勤日"
    verbose_name_plural = "出勤予定一覧"

@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'height', 'joining_date', 'x_url', 'instagram_url', 'display_tags')
    search_fields = ('name', 'comment', 'x_url', 'instagram_url')
    inlines = [WorkScheduleInline]  # インラインに出勤予定を追加

    # タグ表示メソッド
    def display_tags(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())
    display_tags.short_description = 'タグ'