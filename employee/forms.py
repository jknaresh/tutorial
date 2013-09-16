from django import forms

class UploadFileForm(forms.Form):
    thum  = forms.FileField()