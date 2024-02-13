from django.shortcuts import render
from django.views.generic import View
# Create your views here.
class home_page(View):
    def get(self,request):
        return render(request,'frontend/index.html')