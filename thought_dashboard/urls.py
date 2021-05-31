from django.urls import path
from . import views


urlpatterns = [
    path('', views.reg_or_login),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('login', views.login),
    path('add_thought', views.add_thought),
    path('add_like/<id>', views.add_likes),
]