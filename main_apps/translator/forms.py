from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    target_lang = forms.ChoiceField(choices=[
        ("fr", "Français"),
        ("en", "Anglais"),
        ("es", "Espagnol"),
        ("ar", "Arabe"),
    ])
