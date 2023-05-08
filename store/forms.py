from django import forms
from django.views.decorators.csrf import csrf_exempt
from .models import Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment'] 