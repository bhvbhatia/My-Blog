from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog, Comment


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields =  ('author','text')

class PostForm(forms.ModelForm):


    class Meta():
        model = Blog
        fields = ('name','title','body','pub_date')


    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['pub_date'].widget.attrs['class'] = 'form-control'


        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),

        }
