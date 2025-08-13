from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('faq/',faq,name='faq'),
    path('jobs/',jobs,name='jobs'),
]