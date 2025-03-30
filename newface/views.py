from django.shortcuts import render
from list.models import Therapist

def therapist_new_list(request):
    # NEWタグがついたデータをフィルタリング
    new_therapists = Therapist.objects.filter(is_new=True)
    return render(request, 'new_list.html', {'therapists': new_therapists})