# load path
# load views from the same directory

from django.urls import path
from . import views
# set the / api, as variable=index to callback function
urlpatterns = [
    path("index", views.index, name="index"),
    path("about", views.about, name="about"),
    path("", views.index, name="index"),
]
