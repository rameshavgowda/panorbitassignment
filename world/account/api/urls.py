from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('signin', views.Signup, basename='usersignin')
router.register('login', views.login, basename='userlogin')
# router.register('logout',views.logout, basename='logout')



urlpatterns = [
    path ('', include(router.urls))
    # path('signup/',views.Signup.as_view()),
    # path('login/',views.longin.as_view()),
    
]
