from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CustomUserCreationForm

# Create your views here.
def login_user(request):
    if (request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            return (redirect("mangalib:manga"))
        else:
            messages.info(request, "Invalid username or password")
    form = AuthenticationForm()
    return (render(request, "accounts/login.html", {"form": form}))

def logout_user(request):
    logout(request)
    return (redirect("mangalib:manga"))

def register_user(request): 
    if (request.method == "POST"):
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            messages.success(request, "Utilisateur créé avec succès.")
            return (redirect("mangalib:manga"))
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    return (render(request, "accounts/register.html", {"form": form}))