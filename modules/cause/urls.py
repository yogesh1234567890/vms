from django.urls import path
from .views.cause_views import index,fronts

urlpatterns = [
    path('',index),
    path('front/',fronts),
]
