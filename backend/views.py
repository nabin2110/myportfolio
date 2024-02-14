from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.views.generic import View,ListView,DeleteView,UpdateView,CreateView,DetailView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Setting,Service,AboutMe,SocialSite
from backend.forms import SettingForm,AboutMeForm,SocialSiteForm
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
class LoginRequired(LoginRequiredMixin):
    login_url=reverse_lazy('backend:backend_portfolio_login')
    
    
class admin_login(View):
    def get(self,request):
        return render(request,'backend/adminlogin.html')
    
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        if username or password:
            en=authenticate(username=username,password=password)    
            if en:
                return redirect(reverse("backend_portfolio_home"))
            else:
                messages.error(request,"Invalid username/Password")
                return redirect(reverse("backend_portfolio_login"))
        else:
            messages.error(request,'Please Enter Your username/password')
            return redirect(reverse('backend_portfolio_login'))    
        
@method_decorator(login_required,name="dispatch")
class admin_home(LoginRequired,View):
    def get(self,request):
        return render(request,'backend/home.html')        
    
def logout_user(request):
    logout(request)
    messages.success(request,'Logout Success')
    return redirect(reverse('backend_portfolio_login'))


#setting 
model_name=Setting 
path_name="backend/setting"
class SettingCreateView(CreateView):
    def get(self,request):
        fm=SettingForm()
        settingcount=Setting.objects.all()
        if len(settingcount) >0:
            setting=Setting.objects.first()
            return redirect(f'/backendportfolioofnabin/backend/setting/{setting.pk}/detail/')
        return render(request,f'{path_name}/create.html',{'form':fm})   
    
    def post(self, request):
        fm = SettingForm(request.POST, request.FILES)

        if fm.is_valid():
            site_title = request.POST.get('site_title')
            address = request.POST.get('address')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            birthday = request.POST.get('birthday')
            logo_header = request.FILES.get('logo_header')
            main_image = request.FILES.get('main_image')
            fav_icon = request.FILES.get('fav_icon')
            try:
                en = Setting(
                    site_title=site_title,
                    address=address,
                    email=email,
                    phone=int(phone),
                    birthday=birthday,
                    logo_header=logo_header,
                    main_image=main_image,
                    fav_icon=fav_icon
                ).save()
                print(en)
                if en:
                    print('test')
                    messages.success(request, 'Setting Created Successfully')
                    return redirect(reverse('backend_setting_detail'))
                else:
                    print('yes')
                    messages.error(request, 'Failed to save setting.')
                    return redirect(reverse('backend_setting_create'))
            except Exception as e:
                messages.error(request,str(e))
                return redirect(reverse('backend_setting_create'))

        else:
            # Form is not valid, handle the case accordingly
            return render(request, f'{path_name}/create.html', {'form': fm})    
class SettingDetailView(DetailView):
    model=model_name
    context_object_name='record'
    template_name=f'{path_name}/detail.html'

class SettingUpdateView(UpdateView):
    model=model_name
    fields="__all__"
    template_name=f'{path_name}/update.html'
    
    
model_name=Service   
path_name='backend/service'
class ServiceCreateView(SuccessMessageMixin,CreateView):
    model=model_name
    fields='__all__'
    success_message="Data Stored Successfully"
    template_name=f'{path_name}/create.html'
    
    
class ServiceUpdateView(SuccessMessageMixin,UpdateView):
    model=model_name
    fields='__all__'
    success_message="Data Updated Successfully"
    template_name=f'{path_name}/update.html'
    
    
class ServiceDetailView(DetailView):
    model=model_name
    context_object_name='record'
    template_name=f'{path_name}/detail.html'
class ServiceDeleteView(SuccessMessageMixin,DeleteView):
    model=model_name
    success_message='Data Deleted Successfully'
    success_url='/backendportfolioofnabin/backend/service/'
class ServiceListView(ListView):
    model=model_name
    context_object_name='records'
    template_name=f'{path_name}/list.html'    
    
#aboutme

#aboutme 
model_name=AboutMe 
path_name="backend/aboutme"
class AboutMeCreateView(CreateView):
    def get(self,request):
        fm=AboutMeForm()
        aboutme=AboutMe.objects.all()
        if len(aboutme) >0:
            aboutmedetail=AboutMe.objects.first()
            return redirect(f'/backendportfolioofnabin/backend/aboutme/{aboutmedetail.pk}/detail/')
        return render(request,f'{path_name}/create.html',{'form':fm})   
    
    def post(self, request):
        fm = AboutMeForm(request.POST)
        if fm.is_valid():
            title = request.POST.get('title')
            name=request.POST.get('name')
            description=request.POST.get('description')
            try:
                en = AboutMe(
                    title=title,name=name,description=description).save()
                print(en)
                if en:
                    print('test')
                    messages.success(request, 'About Me Created Successfully')
                    return redirect(reverse('backend_aboutme_detail'))
                else:
                    print('yes')
                    messages.error(request, 'Failed to save aboutme.')
                    return redirect(reverse('backend_aboutme_create'))
            except Exception as e:
                messages.error(request,str(e))
                return redirect(reverse('backend_aboutme_create'))

        else:
            # Form is not valid, handle the case accordingly
            return render(request, f'{path_name}/create.html', {'form': fm})    
class AboutMeDetailView(DetailView):
    model=model_name
    context_object_name='record'
    template_name=f'{path_name}/detail.html'

class AboutMeUpdateView(UpdateView):
    model=model_name
    fields="__all__"
    template_name=f'{path_name}/update.html'
    
    #socialsite 
model_name=SocialSite 
path_name="backend/socialsite"
class SocialSiteCreateView(SuccessMessageMixin,CreateView):
  model=model_name
  fields="__all__"
  success_message="Data inserted Successfully"
  template_name=f'{path_name}/create.html'
  
  
class SocialSiteDetailView(DetailView):
    model=model_name
    context_object_name='record'
    template_name=f'{path_name}/detail.html'

class SocialSiteUpdateView(SuccessMessageMixin,UpdateView):
    model=model_name
    fields="__all__"
    success_message="Data updated Successfully"
    template_name=f'{path_name}/update.html'
    
class SocialSiteListView(ListView):
    model=model_name
    context_object_name='records'
    template_name=f'{path_name}/list.html'    
    
class SocialSiteDeleteView(SuccessMessageMixin,DeleteView):
    model=model_name
    success_url='/backendportfolioofnabin/backend/socialsite/'
    success_message="Data deleted successfullys"