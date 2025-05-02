from django.urls import path
from . import views, admin
from .views import checklist_dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.trolley_checklist_view, name='checklist'),
    path('export-csv/', views.export_trolley_csv, name='export_csv'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', checklist_dashboard, name='checklist_dashboard'),
]

