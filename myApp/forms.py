from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'body')

class ContactForm(forms.Form):
  full_name = forms.CharField(max_length = 50)
  address = forms.CharField(max_length = 50)
  phone_number = forms.CharField(max_length = 50)
  email_address = forms.EmailField(max_length= 150)
  work_needed = forms.CharField(widget = forms.Textarea, max_length = 2000)