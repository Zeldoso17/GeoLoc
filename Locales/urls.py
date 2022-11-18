from django.urls import path
from Locales import views

urlpatterns = [
    path('getPlaces/<str:query>', views.getPlaces.as_view(), name='getLocales'),
    path('getPlaceInfo/<int:pk>', views.getPlaceInfo.as_view(), name='getLocalesinfo'),
    path('getPlace/', views.getPlace.as_view(), name='getlocal'),
    path('getClaseActividad/', views.getClaseActividadValues.as_view(), name='getClaseActividad')
]
