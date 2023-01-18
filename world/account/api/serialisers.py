from rest_framework import serializers
from account.models import User, Profile
from account.forms import GENDER_CHOICES
from account.helper import MessageHandler
import random
email = ''
mobilenumber =0

class Userserialiser(serializers.ModelSerializer):
    Gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = User
        fields = ['email','First_name','Last_name','Gender','Mobile_number']

class UserLoginserialiser(serializers.ModelSerializer):
    otp = serializers.SerializerMethodField()
    user_id= serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ['Mobile_number','otp','user_id']

    def validate(self, value):
        global email, mobilenumber
        mn = value.get('Mobile_number')
        print(mn)
        mobilenumber= mn
        mn1=User.objects.get(mobile_number = mn)
        if mn == mn1:
            email= User.objects.values_list('email').get(mobile_number=mn)
            print(email)
        return  

    def get_user_id(self,value):
        value.user_id= email
        return value.user_id
        
    def get_otp(self,value):
        otp=random.randint(1000,9999)
        messagehandler=MessageHandler(mobilenumber,otp).send_otp_via_message()
        return value.otp
    
    def validate_Mobile_number(self,value):
        mobile = value.get('Mobile_number')
        if mobile != mobilenumber:
            raise serializers.ValidationError("Invalide mobile number , If you are first time then signin")
        return value

    def validate(self,value):
        mobile = value.get('Mobile_number')
        mobile1= Profile.objects.get(Mobile_number=mobile)
        if mobile == mobile1:
            raise serializers.ValidationError("OTP allready sent check with your message box")
        return 
