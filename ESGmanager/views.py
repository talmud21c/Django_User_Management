from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import ESGData


def user_page(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    activity_list = ESGData.objects.filter(user=page_user)
    return render(request, 'user_page.html', {
        'page_user': page_user,
        'activity_list': activity_list,
    })