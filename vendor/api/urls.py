from django.urls import path, include

app_name = 'vendor-api'

urlpatterns = [
    path('v1/', include('vendor.api.v1.urls'))
]
