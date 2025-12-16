from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .fruit_list import fruits
from django.shortcuts import redirect

# Create your views here.
def send_fruits(request):
    return  HttpResponse("Hats geklappt oder whats?")

def send_fruits(request):
    return JsonResponse(fruits, safe=False)