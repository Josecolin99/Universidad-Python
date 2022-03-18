from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona


class PersonaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        # asi vuelves tus campos no requeridos
        self.fields['email'].required = False

    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': TextInput(attrs={'type': 'email', 'name': 'aaa'})
        }
