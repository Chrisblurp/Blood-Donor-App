from django.urls import path
from .views import (
    CreateBloodRequestView,
    AdminBloodRequestListView,
    UpdateBloodRequestStatusView,
    StatsAPIView,
    HealthCheckView
)

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="health"),
    path("api/stats/", StatsAPIView.as_view(), name="stats"),
    path("request/create/", CreateBloodRequestView.as_view(), name="create-blood-request"),
    path("admin/blood/requests/", AdminBloodRequestListView.as_view(), name="admin-blood-request-list"),
    path("admin/blood/request/<int:pk>/status/", UpdateBloodRequestStatusView.as_view(), name="update-blood-request-status"),
]
