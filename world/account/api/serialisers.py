from rest_framework import serializers
from account.models import User, Profile
from account.forms import GENDER_CHOICES
from account.helper import MessageHandler

# mobile_number = User.objects.get(mobile_number= request.date('Mobile_number'))

class Userserialiser(serializers.ModelSerializer):
    Gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = User
        fields = ['email','First_name','Last_name','Gender','Mobile_number']

# class UserLoginserialiser(serializers.ModelSerializer):
#     user_id= serializers.SerializerMethodField('_get_email')
#     def _get_email(self, user_objects):
#         email = getattr(user_objects, "email")
#         return email

#     class Meta:
#         model = Profile
#         fields = ['Mobile_number','user_id']

    # def validate_Mobile_number(self,value):
    #     number = User.objects.get(Mobile_number=value)
    #     print(number)
    #     if number != value :
    #         raise serializers.ValidationError("Invalid mobile number")
    #     return value

