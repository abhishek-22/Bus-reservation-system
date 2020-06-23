from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.busbooking, name='busbooking'),
    path('seat/<id>/', views.seat, name='seat'),
    path('bookconf/<id>/', views.bookingconf, name='bookcnf'),
    path('bookinghistory/', views.bookinghist, name='bookinghist'),
    path('bookingcancel/<id>/', views.bookingcancel, name='bookingcancel')
    
]
