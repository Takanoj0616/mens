from django.contrib import admin

from django.contrib import admin
from .models import Topic, Topic2

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    ordering = ('-created_at',)
    
@admin.register(Topic2)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    ordering = ('-created_at',)