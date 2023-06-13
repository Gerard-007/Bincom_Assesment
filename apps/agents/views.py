from django.shortcuts import render
from .models import AgentName


def agent_list(request):
    agents = AgentName.objects.all()
    return render(request, 'agent_list.html', {'agents': agents})
