from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ReservationForm


# View baseada em função
def hello_world(request):
    return HttpResponse('Hello, World!')


# View baseada em classe
class HelloWorld(View):
    def get(self, request):
        return HttpResponse('Hello, World!')


def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponse('Success')

    return render(request, 'index.html', {'form': form})
