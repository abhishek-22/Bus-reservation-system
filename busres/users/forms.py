from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username','first_name' ,'last_name','email','password1','password2']
class booking():
    start = forms.CharField(label='From', max_length=100)
    to = forms.CharField(label='To', max_length=100)
    doj = forms.DateField(label='Date of journey')


class ProfileupdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
