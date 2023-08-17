from django.urls import path
from . import views

urlpatterns = [
    #FUNCTION BASED VIEWS
    #path("",views.home,name='home')

    #CLASS BASED VIEWS
    path("",views.home.as_view(),name="home")

]