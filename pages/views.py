from django.shortcuts import render
from django.views import View

# FUNCTION BASED VIEWS
# def home(request):
#     return render(request,"home.html")


#CLASS BASED VIEWS
class home(View):
    def get(self,request):
        return render(request,"home.html")
