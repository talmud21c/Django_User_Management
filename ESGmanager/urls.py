from django.urls import path, re_path
from . import views

app_name = 'ESGmanager'

urlpatterns = [
    re_path(r'^(?P<username>[\w.@+-]+)/', views.user_page, name='user_page'),
]
