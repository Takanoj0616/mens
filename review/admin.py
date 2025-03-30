from django.contrib import admin
from.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('girl', 'customer_name', 'visit_date', 'comment', 'created_at')  # 一覧表示項目
    search_fields = ('girl', 'customer_name', 'comment', 'visit_date')  # 検索対象