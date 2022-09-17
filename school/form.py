from django import forms

class Studenform(forms.Form):
    name = forms.CharField(max_length=100)
    mail = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    price = forms.DecimalField(min_value= 4, max_value=50, max_digits= 4 , decimal_places= 1)