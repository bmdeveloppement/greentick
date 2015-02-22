from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index/index.html', {})


def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'index/dashboard.html', {'user': request.user})
    return redirect('/')
