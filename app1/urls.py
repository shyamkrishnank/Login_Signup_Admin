from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login, name='user_login'),
    path('signup/',views.signup, name='user_signup'),
    path('login/',views.login, name = 'user_login'),
    path('home/',views.home, name='user_home'),
    path('logout/',views.logout, name='user_logout'),
    path('admin_login/',views.admin_login, name='admin_login'),
    path('admin_home/',views.admin_home, name='admin_home'),
    path('admin_adduser/',views.admin_adduser, name='admin_adduser'),
    path('admin_edit/<int:id>',views.admin_edit , name='admin_edit'),
    path('admin_delete/<int:id>',views.admin_delete, name='admin_delete'),
    path('admin_logout/',views.admin_logout, name='admin_logout'),
    
]
