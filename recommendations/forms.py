from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['yorum']
        widgets = {
            'yorum': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Yorumunuzu buraya yazın...'
            })
        }
        labels = {
            'yorum': 'Yorumunuz'
        }
