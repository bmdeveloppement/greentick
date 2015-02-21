from django.shortcuts import render


def index(request):
    return render(request, 'index/index.html', {})


def dashboard(request):
    return render(request, 'index/dashboard.html', {})