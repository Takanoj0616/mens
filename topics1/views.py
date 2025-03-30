from django.shortcuts import render
from .models import Topic, Topic2

def topics_view(request):
        topics = Topic.objects.all().order_by('-created_at')  # 新着順で取得
        return render(request, 'topics.html', {'topics': topics})
    
def topics_view2(request):
        topics = Topic2.objects.all().order_by('-created_at')  # 新着順で取得
        return render(request, 'topics2.html', {'topics': topics})