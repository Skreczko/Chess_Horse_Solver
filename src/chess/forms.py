from django import forms

class BoardForm(forms.Form):
	point = forms.CharField(max_length=7)