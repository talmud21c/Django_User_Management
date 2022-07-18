from django.urls import path, re_path
from . import views

app_name = 'ESGmanager'

urlpatterns = [
    path('activity/<slug:username>/', views.activity_list, name='activity_list'),
    path('totalpoints/<slug:username>/', views.total_points, name='total_points'),
    path('metamask/<slug:username>/', views.metamask, name='metamask'),
]
