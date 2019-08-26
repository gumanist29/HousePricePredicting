from django.shortcuts import render, redirect
from .forms import HomeForm
from .models import Home
from .lnr import Data
from django.contrib import messages
from rest_framework import generics
from .serializers import HomeSerializer
from django.views.generic import CreateView
from Data_mining.views import home
from django.http import HttpResponse
# Create your views here.




def home_view(request):
    next = request.GET.get('next')
    form = HomeForm(request.POST or None)
    if form.is_valid():
        area = form.cleaned_data.get('area')
        seria = form.cleaned_data.get('seria')
        region=form.cleaned_data.get('region')
        rooms = form.cleaned_data.get('rooms')
        floor = form.cleaned_data.get('floor')
        heating = form.cleaned_data.get('heating')
        messages.success(request, f'Your program are ready')
        h = Home(area=area, seria=seria, rooms=rooms, floor=floor, heating=heating)
        a = []
        a.append(h.rooms)
        a.append(h.seria)
        a.append(h.region)
        a.append(h.area)
        a.append(h.heating)
        a.append(h.floor)

        e = []
        e.append(a)
        print(e)

        d = Data.data_min(e)
        prediction = int(d[0])
        print(type(d))
        h.price = prediction
        h.save()
        messages.info(request, f'The Prediction value is { prediction }$')
        if next:
            return redirect(next)
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'home1.html', context)


class HomeList(generics.ListCreateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
