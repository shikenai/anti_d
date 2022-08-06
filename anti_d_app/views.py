from django.shortcuts import render
from anti_d_app.models import DisasterName


# Create your views here.

def index(request):
    return render(request, 'index.html')


def manage_disaster(request):
    disasters = DisasterName.objects.all()
    return render(request, 'manage_disater.html', {
        'disasters': [{
            'name': d.name
        } for d in disasters]
    })