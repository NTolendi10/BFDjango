from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    user = {
        'id': '123',
        'name': 'Nurzhigit',
        'is_authenticated': True
    }
    context= {
        'user': user,
        'status': 1
    }
    return render(request, 'index.html', context=context)

def time_plus(request):
    if request.GET['hours']:
        dt = datetime.now() + timedelta(hours=int(request.GET['hours']))
        return HttpResponse(dt)
    return HttpResponse('null')

def hours_ahead(request, hours):
    dt = datetime.now() + timedelta(hours=hours)
    return HttpResponse(dt)