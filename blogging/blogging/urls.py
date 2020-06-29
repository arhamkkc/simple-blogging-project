"""blogging URL Configuration

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
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('publish_form',views.publish_form,name='publish_form'),
    path('post_list',views.post_list,name='post_list'),
    path('post/<int:id>',views.get_post,name='post'),
    path('delete/<int:id>',views.delete_post,name='delete_post'),
    path('update/<int:id>',views.update,name='update'),
    
]
