from django.urls import path
from recapp import views

urlpatterns=[
    path("rec",views.rec)
]