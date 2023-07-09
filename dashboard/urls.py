from . import views
from leads import views as leads_views
from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path(
        '',
        views.DashboardView.as_view(),
        name='home'
    ),
    path(
        'leads/',
        leads_views.LeadsView.as_view(),
        name='leads'
    )
]
