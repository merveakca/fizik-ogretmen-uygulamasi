from django.urls import path
from . import views

urlpatterns=[
    path('dersler/', views.DersListCreate.as_view(), name='ders-list'),
    path('dersler/<int:pk>/', views.DersRetrieveUpdateDestroy.as_view(), name='ders-detail'),
]