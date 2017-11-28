from django import forms

class EditChoreForm(forms.Form):
    deadline = forms.DateField(help_text = 'When is this chore due?')

    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        return data

class CreateChoreForm(forms.Form):
    title = forms.CharField(help_text = 'Enter a chore name')
    description = forms.CharField(help_text = 'Enter a description')
    created_on = forms.DateField()
    deadline = forms.DateField(help_text = 'When is this chore due?')

    # no longer than 200
    def clean_title(self):
        data = self.cleaned_data['title']
        return data

    # no longer than 500
    def clean_description(self):
        data = self.cleaned_data['description']
        return data
    
    # can't be in the future
    def clean_created_on(self):
        data = self.cleaned_data['created_on']
        return data

    # can't be in the past
    def clean_deadline(self):
        data = self.cleaned_data['deadline']
        return data

class DeleteChoreForm(forms.Form):
    # don't need anything here
