
class EditChoreForm(forms.Form):
    deadline = forms.DateField(help_text = 'When is this chore due?')

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        return data
