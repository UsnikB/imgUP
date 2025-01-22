from django import forms
from .models import Post

class PostFormPicture(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'photo','caption')
        
class PostFormText(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'caption')