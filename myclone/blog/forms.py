from django import forms
from blog.models import Post,Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields=('first_name','last_name','username','email','password1','password2')
        model=get_user_model()

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text','picture')
        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')
        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
