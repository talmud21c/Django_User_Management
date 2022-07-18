from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from .models import ESGData


@login_required
def activity_list(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    if page_user == 'admin':
        activity_list = ESGData.objects.all()
    else:
        activity_list = ESGData.objects.all().filter(user=page_user)
    return render(request, 'activities.html', {
        'page_user': page_user,
        'activity_list': activity_list,
    })


@login_required
def total_points(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    total_points = ESGData.objects.all().filter(user=page_user).aggregate(Sum('poi'))
    return render(request, 'integrationPoint.html', {
        'page_user': page_user,
        'total_points': total_points,
    })


@login_required
def metamask(request, username):
    page_user = get_object_or_404(get_user_model(), username=username, is_active=True)
    return render(request, 'connectWallet.html', {
        'page_user': page_user,
    })
