from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.liste, name='liste'),
    path('nouveau/', views.nouveau, name='nouveau'),
    path('<code>', views.redirection, name="redirection")
]
