from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
]
