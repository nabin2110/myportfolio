from django.db import models
from django.urls import reverse
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
        