from django.shortcuts import render
from .serialisers import Userserialiser
from account.models import User, Profile
from rest_framework import viewsets
from rest_framework import response


class Signup(viewsets.ModelViewSet):
    serializer_class = Userserialiser

    def get_queryset(self):
        user = User.objects.all()
        return user

    # def create(self, request, *args, **kwargs):
    #     response =  super().create(request, *args, **kwargs)

    #     response.set_COOKIE('Mobile_number',request.date.get('Mobile_number'))
    #     print(request.COOKIES.get('Mobile_number'))
    #     return response

# class login(viewsets.ModelViewSet):
#     serializer_class = UserLoginserialiser

#     def get_queryset(self):
#         profile = Profile.objects.all()
#         return profile
# class longin(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class= UserLoginserialiser