from datetime import date

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publish_date', 'genre', 'quantity']
        widgets = {
            'publish_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_publish_date(self):
        publish_date = self.cleaned_data.get('publish_date')
        if publish_date > date.today():
            raise forms.ValidationError("Publish date cannot be in the future.")
        return publish_date