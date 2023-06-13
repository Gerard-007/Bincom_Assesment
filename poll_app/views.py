import json

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from apps.polling_results.forms import PartyResultForm
from apps.polling_results.models import AnnouncedPUResults
from apps.polling_units.models import PollingUnit, LGA, State, PartyResult


class Home(View):
    def get(self, request):
        polling_units = PollingUnit.objects.all()
        return render(request, "index.html", context={"polling_units": polling_units})

    def post(self, request):
        uniqueid = request.POST.get("uniqueid")
        print(uniqueid)
        results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid=uniqueid)
        return JsonResponse({
            'results': list(results),
            "status": "success",
            "message": "Result fetched successfully."
        })


class LGATotalResult(View):
    def get(self, request):
        states = State.objects.all()
        return render(request, 'lga_select.html', {'states': states})

    def post(self, request):
        lga_id = request.POST.get('lga')
        print(f'lga_id: {lga_id}')
        lga = get_object_or_404(LGA, uniqueid=lga_id)
        polling_units = PollingUnit.objects.filter(lga=lga)
        results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid__in=polling_units)
        total_result = {}
        for result in results:
            if result.party_abbreviation in total_result:
                total_result[result.party_abbreviation] += result.party_score
            else:
                total_result[result.party_abbreviation] = result.party_score
        return JsonResponse(total_result)


class CreatePollingUnit(View):
    def get(self, request):
        form = PartyResultForm()
        return render(request, 'create_polling_unit.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = PartyResultForm(request.POST)
            if form.is_valid():
                polling_unit = form.save()  # Save the polling unit information
                party_results = form.cleaned_data['party_results']  # Get the party results from the form
                # Create PartyResult objects for each party result and associate them with the polling unit
                for party, result in party_results.items():
                    PartyResult.objects.create(polling_unit=polling_unit, party=party, result=result)
                response_data = {
                    'polling_unit_id': polling_unit.id,
                    'party_results': [
                        {'party': party, 'result': result}
                        for party, result in party_results.items()
                    ]
                }
                return JsonResponse(response_data)
        else:
            form = PartyResultForm()
        return render(request, 'create_polling_unit.html', {'form': form})


class GetStateLGA(View):
    def post(self, request):
        state_id = request.POST.get('stateId')
        lgas = LGA.objects.filter(state_id=state_id)
        lgas_data = json.loads(serialize('json', lgas))
        print(f"lgas_data: {lgas_data}")
        return JsonResponse({
            "status": "success",
            "lgas": lgas_data,
            "message": "Data fetched successfully"
        })
