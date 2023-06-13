from django.shortcuts import render
from apps.polling_units.models import LGA, Party, PollingUnit, State, Ward


def lga_list(request):
    lgas = LGA.objects.all()
    return render(request, 'lga_list.html', {'lgas': lgas})


def party_list(request):
    parties = Party.objects.all()
    return render(request, 'party_list.html', {'parties': parties})


def polling_unit_list(request):
    polling_units = PollingUnit.objects.all()
    return render(request, 'polling_unit_list.html', {'polling_units': polling_units})


def state_list(request):
    states = State.objects.all()
    return render(request, 'state_list.html', {'states': states})


def ward_list(request):
    wards = Ward.objects.all()
    return render(request, 'ward_list.html', {'wards': wards})
