from django import forms

class OperationForm(forms.Form):
    num1=forms.CharField()
    num2=forms.CharField()
# for find cubes

class CubeForm(forms.Form):
    num=forms.CharField()

class SquareForm(forms.Form):
    num=forms.CharField()

class EbillForm(forms.Form):
    consumernumber=forms.CharField()
    email=forms.EmailField()
    date=forms.DateField()
    previousreading=forms.CharField()
    currentreading=forms.CharField()

