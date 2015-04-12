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

  def clean_nameType(self):
    valueL = self.cleaned_data['typeLanguage']
    value = self.cleaned_data['nameType']
    t = Type.objects.filter(nameType=value, typeLanguage__nameLanguage=valueL)
    if len(t)>0:
      raise forms.ValidationError("There's already a type with that name for that language in the DB.")
    return value

class ChapterForm(forms.ModelForm):
  class Meta:
    model = Chapter 

  def clean_nameChapter(self):
    valueL = self.cleaned_data['chapterLanguage']
    valueT = self.cleaned_data['chapterType']
    value = self.cleaned_data['nameChapter']
    c = Chapter.objects.filter(nameChapter=value, chapterType__nameType=valueT, chapterLanguage__nameLanguage=valueL)
    if len(c)>0:
      raise forms.ValidationError("There's already a chapter with that name for that type and language in the DB.")
    return value

class UpdateChapterForm(forms.ModelForm):
  class Meta:
    model = UpdateChapter 
