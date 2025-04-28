from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request

from .models import Therapist

#一覧
def therapist_list(request):
    therapists = Therapist.objects.all()
    return render(request, 'list.html', {'therapists': therapists})

#詳細
def therapist_profile(request, id):
    therapist = get_object_or_404(Therapist, id=id)
    return render(request, 'profile.html', {'therapist': therapist})

#待ち時間
def realtime_now(request):
    therapists = Therapist.objects.all()
    return render(request, 'realtime.html', {'therapists': therapists})

