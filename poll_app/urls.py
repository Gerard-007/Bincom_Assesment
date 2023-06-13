from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from poll_app.views import Home, LGATotalResult, GetStateLGA, CreatePollingUnit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(Home.as_view()), name='home'),
    path('lga_total_result/', csrf_exempt(LGATotalResult.as_view()), name='lga_total_result'),
    path('get_state_lga/', csrf_exempt(GetStateLGA.as_view()), name='get_state_lga'),
    path('create_polling_unit/', csrf_exempt(CreatePollingUnit.as_view()), name='create_polling_unit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

admin.site.site_header = "Polling Admin"
admin.site.site_title = "Polling Admin Portal"
admin.site.site_title = "Welcome to the Polling administration"
