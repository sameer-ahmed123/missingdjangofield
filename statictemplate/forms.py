from django import forms
from statictemplate.models import Contact

class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"