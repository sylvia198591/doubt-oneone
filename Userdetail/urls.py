
"""OnlineMobileShop URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.shortcuts import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Userdetail import views
# from Userdetail.views import *
from Userdetail.views import *
# from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
    path("register", views.createUser.as_view(), name="register"),
    # path("login", userLogin, name="login"),
    # path("login", views.LoginView.as_view(), name="login"),
    # path("login", views.LoginView.as_view(), name="login"),
    path('', userHome, name="userhome"),
    path('login', views.LoginView.as_view(), name='login'),
    path('upd/<int:pk>', views.userUpdate.as_view(), name='upd'),
    path("userlogout", userLogout, name="userlogout"),
    path("editprofile", editUserDetails, name="editprofile"),
    # path("viewmobiledetails<int:pk>", viewMobileDetails, name="mobiledetails"),

]
