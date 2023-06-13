from django.urls import path
from . import views

urlpatterns = [
    path('agents/', views.agent_list, name='agent_list'),
]
