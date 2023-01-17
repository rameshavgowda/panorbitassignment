from django import forms
from . models import User, Profile


GENDER_CHOICES =(
    ("Male", "Male"),
    ("Female", "Female"),
    ("Transgender", "Transgender"),
)

class UserForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta: 
        model=User
        fields=['email','First_name','Last_name','Gender','Mobile_number']
        labels={'email':'Email'}
        widgets = {
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'First_name':forms.TextInput(attrs={'class':"form-control"}),
            'Last_name':forms.TextInput(attrs={'class':"form-control"}),
            'Mobile_number':forms.NumberInput(attrs={'class':"form-control"})
        }
      
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Mobile_number']
        labels = {'Mobile_number': 'Enter your mobile no'}
        widgets = {
            'Mobile_number':forms.NumberInput(attrs={'class':'form-control'})
        }
        error_messages ={
            'Moble_number':{'required':'please enter the mobile number'}
        }
class VerifyForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['otp']
        labels = {'otp': 'Enter OTP'}
        widgets = {
            'otp':forms.NumberInput(attrs={'class':'form-control'})
        }
        error_messages ={
            'otp':{'required':'please enter OTP to verify the login'}
        }