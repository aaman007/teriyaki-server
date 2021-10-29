from django.urls import path, include

app_name = 'order-api'

urlpatterns = [
    path('v1/', include('order.api.v1.urls'))
]
