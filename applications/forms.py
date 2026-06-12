import re

from django import forms

from applications.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('client_name', 'phone', 'email', 'title', 'text')
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
            'phone': forms.TextInput(attrs={
                'type': 'tel',
                'placeholder': '+7(___)___-__-__',
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        digits = re.sub(r'\D', '', phone)
        return digits
