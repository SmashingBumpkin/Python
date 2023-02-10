from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login
from recipes.forms import CustomUserCreationForm


# def index(request):
#     return HttpResponse("Hello, world. You're at the kitchen life homepage")

def index(request):
    return render(request, 'kitchenlife\index.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "kitchenlife/register.html",
            {"form": CustomUserCreationForm}
        )

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))