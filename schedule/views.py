from django.shortcuts import render
from datetime import datetime
from list.models import Therapist

def schedule_view(request):
    today = datetime.now().date()
    therapists = Therapist.objects.filter(schedules__date=today).distinct()
    
    context = {
        'therapists': therapists,
        'today': today,
    }
    return render(request, 'schedule.html', context)