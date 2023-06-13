from django.shortcuts import render
from .models import AnnouncedLgaResult, AnnouncedPuResult, AnnouncedStateResult, AnnouncedWardResult


def announced_lga_result_list(request):
    results = AnnouncedLgaResult.objects.all()
    return render(request, 'announced_lga_result_list.html', {'results': results})


def announced_pu_result_list(request):
    results = AnnouncedPuResult.objects.all()
    return render(request, 'announced_pu_result_list.html', {'results': results})


def announced_state_result_list(request):
    results = AnnouncedStateResult.objects.all()
    return render(request, 'announced_state_result_list.html', {'results': results})


def announced_ward_result_list(request):
    results = AnnouncedWardResult.objects.all()
    return render(request, 'announced_ward_result_list.html', {'results': results})
