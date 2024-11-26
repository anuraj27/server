#shopify_atats/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('', include('users.urls')),
    #path('users/', include('oauth.urls')),
]
