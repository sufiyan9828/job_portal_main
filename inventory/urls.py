from django.urls import path
from .views import *

urlpatterns=[
    path('jobs/',jobs,name='jobs'),
    # path('posts/',posts,name='posts'),
    path('posts/',Post.as_view(),name="posts"),

]