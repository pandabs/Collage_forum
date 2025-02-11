# forum/forms.py
from django import forms
from .models import Forum, Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['title', 'description']  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'image']  