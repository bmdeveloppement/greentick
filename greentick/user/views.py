from django.shortcuts import render, get_object_or_404

from user.models import User


def index(request):
    return render(request, 'index/index.html', {})


def edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user/edit.html', {'user': user})
