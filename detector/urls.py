# detector/urls.py
from django.urls import path
from . import views

app_name = 'detector'

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('history/', views.history, name='history'),
    path('about/', views.about, name='about'),
    path('api/history/count/', views.history_count, name='history_count'),
]