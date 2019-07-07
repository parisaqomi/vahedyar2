"""vahedyar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index , name='index'),
    path('panel/<int:study_id>/', views.get_panel, name='dashboard'),
    path('courseAssistant', views.get_courseAssistant, name='courseAssistant'),
    path('courseList/<int:study_id>/', views.get_courseList, name='courseList'),
    path('courseSituation/<int:study_id>/', views.get_courseSituation, name='courseSituation'),
    path('ftForm', views.get_ftForm , name='ftForm'),
    path('login', views.do_login , name='login'),
    path('logout', views.do_logout , name='logout'),
    path('404', views.get_404),
    path('updateScore/<int:study_id>/<int:course_id>/', views.create_or_update_score, name='updateScore')
]
