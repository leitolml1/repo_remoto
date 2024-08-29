from django import forms
from .models import Post,Comment

class CrearPost(forms.ModelForm):
    class Meta:
        model=Post
        fields=['titulo','contenido']

class AgregarComentario(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['autor','contenido']



