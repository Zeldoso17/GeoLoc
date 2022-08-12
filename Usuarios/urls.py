from django.urls import path
from Usuarios import views

urlpatterns = [
    path('auth/createUser/', views.CreateUser.as_view(), name='crearUsuario'),
    path('auth/login/', views.LoginUser.as_view(), name='loginUser'),
    path('auth/logout/', views.LogoutUser.as_view(), name='logoutUser'),
    path('CSRF/', views.GetCSRFToken.as_view(), name='csrfToken')
]
