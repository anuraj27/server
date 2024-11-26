from django.urls import path, include
from . import views

# urlpatterns = [
#     path('', views.home),
#     path('dashboard', views.dashboard),
# ]

urlpatterns = [
    path('login/', views.login, name='login'),
    path('callback/', views.callback, name='callback'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
]
