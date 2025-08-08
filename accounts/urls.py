from django.urls import path
from .views import *
urlpatterns = [
    path('accounts/register/',Register.as_view(),name="register"),
    path('accounts/login/',Login.as_view(),name="login"),
    path('logout/',Logout.as_view(),name="logout"),
]