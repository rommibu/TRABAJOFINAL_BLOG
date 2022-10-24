from django import forms

class FormMensajes(forms.Form):
    mensahe=forms.CharField(widget=forms.Textarea(attrs={
        
        "class": "formulario_ms",
        "placeholder":"Escribe tu chisme"
    }))