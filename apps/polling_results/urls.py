from django.urls import path
from . import views

urlpatterns = [
    path('announced_pu_results/', views.announced_pu_result_list, name="announced_pu_results"),
    path('announced_lga_results/', views.announced_lga_result_list, name="announced_lga_results"),
    path('announced-state-results/', views.announced_state_result_list, name='announced_state_results'),
    path('announced-ward-results/', views.announced_ward_result_list, name='announced_ward_results'),
]
