from django import forms
from .models import PostingUser
from django.contrib.auth.forms import UserCreationForm

#
# class PostingForm(forms.Form):
#     name = forms.CharField(label = "Название поста", max_length = 100)
#     text = forms.CharField(label = "Текст поста", max_length = 1000)
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())

class RegistrationUserForm(UserCreationForm):

    class Meta:
        model = PostingUser
        #fields = '__all___'
        fields=('username', 'password', 'email')
