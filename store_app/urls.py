from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('user_profile/', views.user_profile, name='user_profile'),
    # Ajax request
    path('load_courses/', views.load_courses, name='load_courses'),
    path('logout/',views.logout, name='logout'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation')

]
