from django import forms
from .models import Tag, My_post
#
# class PostingForm(forms.Form):
#     name = forms.CharField(label = "Название поста", max_length = 100)
#     text = forms.CharField(label = "Текст поста", max_length = 1000)
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())

class PostingForm(forms.ModelForm):
    my_post_name = forms.CharField(label = "Название статьи")
    class Meta:
        model = My_post
        fields = '__all__'
        # fields=('my_post_name', 'my_post_text')
