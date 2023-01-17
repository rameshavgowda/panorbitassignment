from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('sign/',views.sign_up, name="sign_up"),
    path('', views.Log_in, name='login'),
    path('otp/<str:uid>/', views.otpverify, name='otp'),
    path('logout/', views.otp_logout, name='logout'),
]