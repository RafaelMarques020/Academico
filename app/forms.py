from django import forms
from .models import Pessoa
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome', 
            'pai', 
            'mae', 
            'cpf', 
            'data_nasc', 
            'email', 
            'cidade', 
            'ocupacao',
            Submit('submit', 'Salvar')
        )