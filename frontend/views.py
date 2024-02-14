from django.shortcuts import render
from django.views.generic import View,CreateView
from backend.models import Service,Contact
from django.contrib.messages.views import SuccessMessageMixin# Create your views here.
class home_page(View):
    def get(self,request):
        context={
            'services':Service.objects.all(),
        }
        return render(request,'frontend/index.html',context)
    
class resume_page(View):
    def get(self,request):
        return render(request,'frontend/resume.html')
    
    
class contact_page(SuccessMessageMixin,CreateView):
    model=Contact
    fields='__all__'
    success_message="Your message sent successfully"
    template_name='frontend/contact.html'