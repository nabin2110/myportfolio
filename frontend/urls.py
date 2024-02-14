from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page.as_view(),name="frontend_homepage"),
    path('resume/',views.resume_page.as_view(),name="frontend_resumepage"),
    path('contact/',views.contact_page.as_view(),name="frontend_contactpage")
]
