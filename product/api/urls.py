from django.urls import path, include

app_name = 'product-api'

urlpatterns = [
    path('v1/', include('product.api.v1.urls'))
]
