from django.urls import path, register_converter, converters
from Locales import views

register_converter(converters.SlugConverter, 'float')

urlpatterns = [
    path('getPlaces/<str:query>', views.getPlaces.as_view(), name='getLocales'),
    path('getPlace/<int:pk>', views.getPlace.as_view(), name='getLocales')
]
