from django import forms


CHOICE = (
    ('low','Low'),
    ('medium','Medium'),
    ('high', 'High')
)


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=500)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    priority = forms.ChoiceField(choices=CHOICE)
    upload_images = MultipleFileField()