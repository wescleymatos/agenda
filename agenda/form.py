from django import forms

class FormItemAgenda(forms.Form):
    data = forms.DateField(
        widgets = forms.DateInput(format = '%d/%m/%Y'),
        input_forms = ['%d/%m/%y', '%d/%m/%Y']
    )
    hora = forms.TimeField()
    titulo = forms.CharField(max_length=100)
    descricao = forms.TextField()

