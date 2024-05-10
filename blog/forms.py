
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Post
from django.utils.translation import gettext, gettext_lazy as _    ##This line only to define label _ in authtication password

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'confirm password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class  Meta:
      model = User


      
      fields = ['username','first_name','last_name','email']
      labels = {'username':'UserName', 'first_name':'First_Name','last_name':'Last_Name', 'email':'Email'}
      widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
              'first_name':forms.TextInput(attrs={'class':'form-control'}),
              'last_name':forms.TextInput(attrs={'class':'form-control'}),
              'email':forms.TextInput(attrs={'class':'form-control'})}


class LogInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

##Post form is for updated form  of the post and not a new one ##
class PostForm(forms.ModelForm):
   class Meta:
      model = Post
      fields = ['title', 'content']
      labels = {'title':'Title', 'content':'Content'} 
      widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                 'content':forms.TextInput(attrs={'class':'form-control'})}   
      

