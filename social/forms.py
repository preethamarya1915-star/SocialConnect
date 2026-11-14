from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile
class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["caption","image"]
        widgets={"caption":forms.Textarea(attrs={"rows":3,"placeholder":"What's happening?"})}
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["bio","avatar"]
class CommentForm(forms.Form):
    body=forms.CharField(max_length=500,widget=forms.TextInput(attrs={"placeholder":"Write a comment..."}))
