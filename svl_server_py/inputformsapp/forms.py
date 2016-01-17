from inputformsapp.models import Language, Type, Chapter, UpdateChapter, Word
from django import forms

class LanguageForm(forms.ModelForm):
  class Meta:
    model = Language
    fields = '__all__'

  def clean_nameLanguage(self):
    value = self.cleaned_data['nameLanguage']
    l = Language.objects.filter(nameLanguage=value)
    if len(l)>0:
      raise forms.ValidationError("There's already a language with that name in the DB.")
    return value

class TypeForm(forms.ModelForm):
  class Meta:
    model = Type 
    fields = '__all__'

  def clean_nameType(self):
    valueL = self.cleaned_data['typeLanguage']
    value = self.cleaned_data['nameType']
    t = Type.objects.filter(nameType=value, typeLanguage__nameLanguage=valueL)
    if len(t)>0:
      raise forms.ValidationError("There's already a type with that name for that language in the DB.")
    return value

class ChapterForm(forms.ModelForm):
  mDl = forms.CharField(required=False)
  mLU = forms.CharField(required=False)
  class Meta:
    model = Chapter 
    fields = '__all__'

  def clean_nameChapter(self):
    valueL = self.cleaned_data['chapterLanguage']
    valueT = self.cleaned_data['chapterType']
    value = self.cleaned_data['nameChapter']
    c = Chapter.objects.filter(nameChapter=value, chapterType__nameType=valueT, chapterLanguage__nameLanguage=valueL)
    if len(c)>0:
      raise forms.ValidationError("There's already a chapter with that name for that type and language in the DB.")
    return value

  def clean_mDl(self):
    data = self.cleaned_data['mDl']
    if not data:
      data = 'false'
    return data

  def clean_mLU(self):
    data = self.cleaned_data['mLU']
    if not data:
      data = 'true'
    return data

class UpdateChapterForm(forms.ModelForm):
  class Meta:
    model = UpdateChapter 
    fields = '__all__'


class WordForm(forms.ModelForm):
  mSuccess = forms.CharField(required=False)
  mSeen = forms.CharField(required=False)
  mProp = forms.CharField(required=False)
  class Meta:
    model = Word
    fields = '__all__'

  def clean_mSuccess(self):
    data = self.cleaned_data['mSuccess']
    if not data:
      data = 0 
    return data

  def clean_mSeen(self):
    data = self.cleaned_data['mSeen']
    if not data:
      data = 0 
    return data

  def clean_mProp(self):
    data = self.cleaned_data['mProp']
    if not data:
      data = 1 
    return data
