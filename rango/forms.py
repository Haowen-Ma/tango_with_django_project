from django import forms
from rango.models import Page,Category
from django.contrib.auth.models import User
from rango.models import UserProfile

class CategoryForm(forms.ModelForm):
    name =forms.CharField(max_length=Category._meta.get_field('name').max_length,
                           help_text="Please enter the category name.")
    views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug =forms.CharField(widget=forms.HiddenInput(),required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError("Category with this Name already exists.")
        return name

    class Meta:
        model=Category
        fields =('name',)

class PageForm(forms.ModelForm):
    title =forms.CharField(max_length=128,
                           help_text="Pleaseenterthetitleofthepage.")
    url =forms.URLField(max_length=200,
                         help_text="PleaseentertheURLofthepage.")
    views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    class Meta:
        model=Page
        exclude= ('category',)   
    def clean(self): 
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User    
        fields = ('username', 'email', 'password',)
class UserProfileForm(forms.ModelForm):
    class Meta:   
        model = UserProfile   
        fields = ('website', 'picture',)  