from inputformsapp.models import Language, Type, Chapter, UpdateChapter
from django import forms

class LanguageForm(forms.ModelForm):
  class Meta:
    model = Language

  def clean_nameLanguage(self):
    value = self.cleaned_data['nameLanguage']
    l = Language.objects.filter(nameLanguage=value)
    if len(l)>0:
      raise forms.ValidationError("There's already a language with that name in the DB.")
    return value

class TypeForm(forms.ModelForm):
  class Meta:
    model = Type 

class ChapterForm(forms.ModelForm):
  class Meta:
    model = Chapter 

class UpdateChapterForm(forms.ModelForm):
  class Meta:
    model = UpdateChapter 
