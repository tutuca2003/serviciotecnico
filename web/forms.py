from django import forms

from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ["nombre", "telefono", "email", "equipo", "problema"]
        widgets = {
            "problema": forms.Textarea(attrs={"rows": 4}),
        }
