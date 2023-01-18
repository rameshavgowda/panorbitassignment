from django.shortcuts import render
from .serialisers import Userserialiser, UserLoginserialiser
from account.models import User, Profile
from rest_framework import viewsets
from django.contrib.auth import logout
from rest_framework import request
from rest_framework.decorators import action


class Signup(viewsets.ModelViewSet):
    serializer_class = Userserialiser

    def get_queryset(self):
        user = User.objects.all()
        return user

class login(viewsets.ModelViewSet):
    serializer_class = UserLoginserialiser

    def get_queryset(self):
        profile = Profile.objects.all()
        return profile

# @action(methods=['get', 'post'])
# class logout(viewsets.ModelViewSet):
#     if 'Mobile_number' in request.session:
#         del request.session['Mobile_number']
#     logout(request)