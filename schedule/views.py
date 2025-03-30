from django.shortcuts import render
from datetime import date
from list.models import Therapist
from django.http import JsonResponse

def schedule_view(request):
    today = date.today().isoformat()
    therapists = Therapist.objects.filter(schedule__icontains=today)
    return render(request, 'schedule.html', {'therapists': therapists, 'today': today})