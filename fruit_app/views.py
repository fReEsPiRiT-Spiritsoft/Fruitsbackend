from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .fruit_list import fruits
from django.shortcuts import redirect

# Create your views here.
# def send_fruits(request):
#     return  HttpResponse("Hats geklappt oder what?")

def send_fruits(request):
    return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})

def info_view(request):
    return render(request, "fruit_app/info.html")

def custom_404(request, exception):
    return render (request, "fruit_app/404.html", status=404)