from django.contrib import admin
from apps.polling_results.models import AnnouncedLGAResults, AnnouncedPUResults, AnnouncedStateResults, \
    AnnouncedWardResults

# Register your models here.
admin.site.register(AnnouncedLGAResults)
admin.site.register(AnnouncedPUResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)
