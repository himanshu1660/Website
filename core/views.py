from django.shortcuts import render
from django.http import HttpResponse 

def index(request):

    return render(request, 'index.html')

def chains(request):
    return render(request, 'chains.html')

def admin(request):
    return render(request, 'admin.html')

def profile(request):
    return render(request, 'profile.html')

def cart(request):
    return render(request, 'cart.html')