from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello, world. You're at the kitchen life homepage")

def index(request):
    return render(request, 'kitchenlife\index.html')