
from django import forms
from .models import TrolleyChecklist

CHOICES = [('OK', 'OK'), ('Not OK', 'Not OK')]

class ColoredSelect(forms.Select):
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        if option['value'] == 'OK':
            option['attrs']['style'] = 'background-color: #d4edda; color: #155724;'
        elif option['value'] == 'Not OK':
            option['attrs']['style'] = 'background-color: #f8d7da; color: #721c24;'
        return option

class TrolleyChecklistForm(forms.ModelForm):
    trolley_no = forms.CharField()
    inspector_name = forms.CharField()

    class Meta:
        model = TrolleyChecklist
        exclude = ['status', 'date_checked','user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically convert checklist fields to choice fields with colored select
        for field_name in self.fields:
            if field_name not in ['trolley_no', 'inspector_name']:
                self.fields[field_name] = forms.ChoiceField(
                    choices=CHOICES,
                    widget=ColoredSelect(),
                    label=self.fields[field_name].label
                )


