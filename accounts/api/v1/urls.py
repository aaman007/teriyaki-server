from django.urls import path

from accounts.api.v1.views import GoogleLogin

app_name = 'accounts-api-v1'

urlpatterns = [
    path('login/google/', GoogleLogin.as_view(), name='google-login')
]
