from django.shortcuts import render, HttpResponse
from anti_d_app.models import DisasterName
from anti_d_app.forms import FormDisaster


# Create your views here.

def index(request):
    return render(request, 'index.html')


def manage_disaster(request):
    disasters = DisasterName.objects.all()
    if request.method == 'POST':
        form = FormDisaster(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    return render(request, 'manage_disater.html', {
        'disasters': [{
            'name': d.name
        } for d in disasters],
        'form': FormDisaster
    })

