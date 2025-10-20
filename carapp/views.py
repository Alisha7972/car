from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, "carapp/car_list.html", {"cars": cars})

def add_car(request):
    if request.method == "POST":
        name = request.POST.get("name")
        brand = request.POST.get("brand")
        year = request.POST.get("year")

        car = Car.objects.create(name=name, brand=brand, year=year)
        return JsonResponse({
            "id": car.id,
            "name": car.name,
            "brand": car.brand,
            "year": car.year
        })
    return JsonResponse({"error": "Invalid request"}, status=400)


def home(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

def models(request):
    return render(request, 'frontend/models.html')

def client_section(request):
    return render(request, 'frontend/client_section.html')

def blog(request):
    return render(request, 'frontend/blog.html')


# Create your views here.
