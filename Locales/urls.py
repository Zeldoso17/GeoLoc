from django.urls import path
from Locales import views

urlpatterns = [
    path('getLocales/', views.listadoLocales.as_view(), name='getLocales'),
    path('getLocal/<int:pk>', views.obtenerLocal.as_view(), name='getLocales')
]
