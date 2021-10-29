from django.urls import path

from core.api.v1.views import PingAPIView

app_name = 'core-api-v1'

urlpatterns = [
    path('ping/', PingAPIView.as_view(), name='ping')
]
