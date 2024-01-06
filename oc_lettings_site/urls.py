from django.contrib import admin
from django.urls import path, include
from oc_lettings_site import views


def trigger_error(request):
    """Make sure that Sentry is working"""
    division_by_zero = 1 / 0


handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
