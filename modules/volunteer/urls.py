from django.urls import path
from .views.volunteer_index import index,fronts



urlpatterns = [
    path('',index),
    path('front/',fronts),
]
