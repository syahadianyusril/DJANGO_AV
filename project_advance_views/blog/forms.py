from django import forms

from .models import Blog

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('image','created_at','judul','konten')