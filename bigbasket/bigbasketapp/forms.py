from django import forms
from django.contrib.auth.models import User
from bigbasketapp.models import userprofile

class customer(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password')                                #'__all__'

class vendor(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = ('ID_proof','user_url')
