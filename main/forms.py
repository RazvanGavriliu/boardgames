from django import forms

class PersonForm(forms.Form):
    nume = forms.CharField()
    email = forms.EmailField(required=False)
    phonenumber = forms.IntegerField()



class PersonsForm(forms.Form):
    nume = forms.CharField()
    email = forms.EmailField(required=False)
    phonenumber = forms.IntegerField()