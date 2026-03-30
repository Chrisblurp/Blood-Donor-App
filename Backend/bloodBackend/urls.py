
from django.urls import path, include
from django.contrib import admin
from django.conf import settings # new
from django.conf.urls.static import static #new
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', include('django_prometheus.urls')),  # Added this
    path("admin/", admin.site.urls), 
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("bloodaccounts.urls")),
    path("api/", include("donoraccounts.urls")),
    path("api/blood/", include("donoraccounts.urls")),
    path("api/", include("blood.urls")),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)