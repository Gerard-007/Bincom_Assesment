from django.urls import path
from . import views

urlpatterns = [
    path('lgas/', views.lga_list, name='lga_list'),
    path('parties/', views.party_list, name='party_list'),
    path('polling_unit_list/', views.polling_unit_list, name='polling_unit_list'),
]
