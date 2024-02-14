from django.db import models
from django.urls import reverse
from django.core.mail import send_mail
# Create your models here.
class Common(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True
        
class Setting(Common):
    site_title=models.CharField(max_length=200)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    birthday=models.CharField(max_length=100)
    logo_header=models.ImageField(upload_to='images/settings/',blank=True,null=True)
    main_image=models.ImageField(upload_to='images/settings/',blank=True,null=True)
    fav_icon=models.ImageField(upload_to='images/settings/',blank=True,null=True)
    
    def __str__(self):
        return self.site_title     
    
    def get_absolute_url(self):
        return reverse("backend_setting_detail", kwargs={"pk": self.pk})
       
class Service(Common):
    icon=models.CharField(max_length=100)
    title=models.CharField(max_length=100,unique=True)
    description=models.TextField()

    def __str__(self):
        return self.title       
    
    def get_absolute_url(self):
        return reverse("backend_service_list")
    
class AboutMe(Common):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.TextField()
    resume=models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("backend_aboutme_detail", kwargs={"pk": self.pk})
        
class SocialSite(Common):
    icon=models.CharField(max_length=100)
    link=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.icon
    
    
    def get_absolute_url(self):
        return reverse("backend_socialsite_list")
    
    
class Contact(Common):
        name=models.CharField(max_length=100)
        email=models.EmailField()
        number=models.CharField(max_length=200)
        subject=models.CharField(max_length=200)
        message=models.TextField()
        
        
        def __str__(self):
            return self.name
        
        
        def get_absolute_url(self):
            send_mail('Hey '+self.name,'Thank you for contacting us '+self.name,'nabinthapaletsgo123@gmail.com',[self.email,],fail_silently=False)
            return reverse('frontend_contactpage')