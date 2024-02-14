from django import forms
from .models import Setting,AboutMe,SocialSite

class SettingForm(forms.ModelForm):
    
    class Meta:
        model=Setting
        fields="__all__"
        widgets={
            'site_title':forms.TextInput(attrs={'class':'form-control','id':"site_title"}),
            'email':forms.EmailInput(attrs={"class":'form-control','id':"email"}),
            'phone':forms.NumberInput(attrs={'class':'form-control','id':'phone'}),
            'address':forms.TextInput(attrs={'class':'form-control','id':'addres'}),
            'hero_image':forms.FileInput(attrs={'class':'form-control','id':'hero_image'}),
            'logo_header':forms.FileInput(attrs={'class':'form-control','id':'logo_header'}),
            'fav_icon':forms.FileInput(attrs={'class':'form-control','id':'fav_icon'}),
            'birthday':forms.TextInput(attrs={'class':"form-control",'id':'birthday'})
        }  
        
class AboutMeForm(forms.ModelForm):
    
    class Meta:
        model=AboutMe
        fields="__all__"
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','id':"title"}),
            'name':forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'description':forms.TextInput(attrs={'class':'form-control','id':'description'}),
            'resume':forms.TextInput(attrs={'class':'form-control','id':'resume'})
        }          
        
class SocialSiteForm(forms.ModelForm):
    
    class Meta:
        model=SocialSite
        fields="__all__"
        widgets={
            'icon':forms.TextInput(attrs={'class':'form-control','id':"icon"}),
            'link':forms.TextInput(attrs={'class':'form-control','id':'link'}),
        }                  