from django.urls import path, include

app_name = 'wishlist-api'

urlpatterns = [
    path('v1/', include('wishlist.api.v1.urls'))
]
