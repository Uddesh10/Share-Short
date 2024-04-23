from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout_user , registration_view

urlpatterns = [
    path('login/' , obtain_auth_token , name='login'),   
    path('register/' , registration_view , name='register'),
    path('logout/' , logout_user , name='logout')
]