from django import forms
from . models import ProductAdding,registrationAdding

class ProductAddingForms(forms.ModelForm):
    class Meta:
        model=ProductAdding
        fields="__all__"


class RegistrationAddingForm(forms.ModelForm):
    class Meta:
        model=registrationAdding
        fields="__all__"

    def clean_full_name(self):
        fullname=self.cleaned_data["full_name"]
        if len(fullname) < 4:
            raise forms.ValidationError("enter a valid name")
        return fullname

    def clean_username(self):
        username=self.cleaned_data["username"]
        if registrationAdding.objects.filter(username=username).exists():
            raise forms.ValidationError("user name alredy exists")
        return username

    def clean_email(self):
        email=self.cleaned_data["email"]
        if registrationAdding.objects.filter(email=email).exists():
            raise forms.ValidationError("user email alredy exists")
        return email

    def clean_password(self):
        password=self.cleaned_data["password"]
        if len(password) < 4:
            raise forms.ValidationError("enter a valid password")
        return password