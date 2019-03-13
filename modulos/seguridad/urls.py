from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import usuario_actual

urlpatterns = [
    path('api/get_token/', obtain_auth_token, name='obtain_auth_token'),
    path('api/me/', usuario_actual, name='usuario_actual')
]