from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_login.as_view(),name="backend_portfolio_login"),
    path('home/',views.admin_home.as_view(),name="backend_portfolio_home"),
    path('logout/',views.logout_user,name="backend_portfolio_logout"),
    #setting path
    path('backend/setting/',views.SettingCreateView.as_view(),name="backend_setting_create"),
    path('backend/setting/<int:pk>/detail/',views.SettingDetailView.as_view(),name="backend_setting_detail"),
    path('backend/setting/<int:pk>/update/',views.SettingUpdateView.as_view(),name='backend_setting_update'),
    #service path
    path("backend/service/create/",views.ServiceCreateView.as_view(),name="backend_service_create"),
    path('backend/service/',views.ServiceListView.as_view(),name="backend_service_list"),
    path('backend/service/<int:pk>/detail/',views.ServiceDetailView.as_view(),name="backend_service_detail"),
    path('backend/service/<int:pk>/update/',views.ServiceUpdateView.as_view(),name="backend_service_update"),
    path('backend/service/<int:pk>/delete',views.ServiceDeleteView.as_view(),name="backend_service_delete"),
    #aboutme
    
    path('backend/aboutme/',views.AboutMeCreateView.as_view(),name="backend_aboutme_create"),
    path('backend/aboutme/<int:pk>/detail/',views.AboutMeDetailView.as_view(),name="backend_aboutme_detail"),
    path('backend/aboutme/<int:pk>/update/',views.AboutMeUpdateView.as_view(),name='backend_aboutme_update'),
]
