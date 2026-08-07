#cars_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})
