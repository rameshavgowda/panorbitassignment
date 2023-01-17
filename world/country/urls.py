from django.urls import path
from country import views

app_name = 'country'

urlpatterns = [
    path('',views.Country_view_search, name= "searchdata"),
    path('countrydetails/<str:code>/', views.countryviewlist, name="countrydetails")
]