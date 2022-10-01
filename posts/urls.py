from django.urls import path
from .views import *

urlpatterns = [
    path("colleges/",CollegeListAPI.as_view()),
]