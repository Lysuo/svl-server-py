from inputformsapp.models import Language, Type, Chapter, UpdateChapter
from django import forms

class LanguageForm(forms.ModelForm):
  class Meta:
    model = Language

class TypeForm(forms.ModelForm):
  class Meta:
    model = Type 

class ChapterForm(forms.ModelForm):
  class Meta:
    model = Chapter 

class UpdateChapterForm(forms.ModelForm):
  class Meta:
    model = UpdateChapter 
