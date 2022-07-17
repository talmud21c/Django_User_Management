from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ESG/', include('ESGmanager.urls')),
    path('accounts/', include('accounts.urls')),
]
