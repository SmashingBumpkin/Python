from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import login
from recipes.forms import CustomUserCreationForm
from recipes.models import Profile


# def index(request):
#     return HttpResponse("Hello, world. You're at the kitchen life homepage")

def index(request):
    money = round(0.002*request.user.profile.ai_credits_used/1000,2)
    return render(request, 'kitchenlife/index.html',{'money': money})

def about(request):
    return render(request, 'kitchenlife/about.html')

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
            profile = Profile.objects.create(user=user)
            profile.save()
            login(request, user)
            return redirect(reverse("index"))