from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from list.models import Therapist
from topics1.models import Topic, Topic2

class SystemView(TemplateView):
    template_name = 'system.html'
    
class RecruitView(TemplateView):
    template_name = 'recruit.html'
    
def index_view(request):
    # NEWタグがついたデータをフィルタリング
    new_therapists = Therapist.objects.filter(is_new=True)
    return render(request, 'index.html', {'therapists': new_therapists})

def topics_view(request):
        topics = Topic.objects.all().order_by('-created_at')  # 新着順で取得
        return render(request, 'topics.html', {'topics': topics})
    

def topics_view2(request):
        topics = Topic2.objects.all().order_by('-created_at')  # 新着順で取得
        return render(request, 'topics2.html', {'topics': topics})