from django.contrib import admin
from apps.polling_units.models import State, LGA, Ward, Party, PollingUnit


# Register your models here.
admin.site.register(State)
admin.site.register(LGA)
admin.site.register(Ward)
admin.site.register(Party)
admin.site.register(PollingUnit)
