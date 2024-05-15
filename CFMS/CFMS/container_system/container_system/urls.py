"""container_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from project_app.views import home
from project_app.views import booking
from project_app.views import track
from project_app.views import details
from project_app.views import about_us
#from project_app.views import register
from project_app.views import signup
#from project_app.views import index, login_view
from project_app.views import user_login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='project_app/login.html'), name='login'),
    path('register/', signup, name='register'),
    path('accounts/profile/', lambda request: redirect('booking'), name='profile_redirect'),
    path('booking/', login_required(booking), name='booking'),
    path('tracking/', track, name='track'),
    path('details/', details, name='details'),
    path('about_us/', about_us, name='about_us'),    
    path('', include("project_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)