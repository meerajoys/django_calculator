
from django.urls import path
from mathsapp import views

urlpatterns = [
    path("add",views.AddView.as_view(),name="addition"),
    path("sub",views.SubView.as_view(),name="subtraction"),
    path("mult",views.mult,name="multiplication"),
    path("div",views.div,name="division"),
    path("wordcount",views.word_count,name="wordcount"),
    path("cube",views.cube,name="cube"),
    path("square",views.square,name="square"),
    path("",views.home,name="home"),
    path("ebill",views.ebill,name="ebill")
]
