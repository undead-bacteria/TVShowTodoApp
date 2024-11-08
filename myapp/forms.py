from django import forms 
from .models import TelevisionShow


class TelevisionShowForm(forms.ModelForm):
  class Meta:
    model = TelevisionShow
    fields = ['title', 'genre', 'release_date', 'description']

    # setting widgets to customize the look of form fields
    widgets = {
      'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
      'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
      'genre': forms.Select(attrs={'class': 'form-control'})
    }

    # csutom validation for the form fields
    def clean_title(self):
      title = self.cleaned_date.get('title')
      if not title:
        raise forms.ValidationError("The title of the show is required.")
      return title
    
    def clean_genre(self):
      genre = self.cleaned_data.get('genre')
      if not genre:
          raise forms.ValidationError("Please select a genre.")
      return genre
    
