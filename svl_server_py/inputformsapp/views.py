from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from datetime import datetime
from inputformsapp.models import Language, Type, Chapter
from inputformsapp.forms import LanguageForm, TypeForm, ChapterForm

# Create your views here.

def home(request):
  if request.method == 'POST':
    formLanguage = LanguageForm(request.POST)
    formType= TypeForm(request.POST)
    formChapter= ChapterForm(request.POST, request.FILES)

    if formLanguage.is_valid():

      language = formLanguage.cleaned_data['nameLanguage']
      icon = formLanguage.cleaned_data['icon']

      sentLanguage = True
      formLanguage.save()

    elif formType.is_valid():

      language = formType.cleaned_data['typeLanguage']
      name = formType.cleaned_data['nameType']

      sentType = True
      formType.save()

    elif formChapter.is_valid():

      language = formChapter.cleaned_data['chapterLanguage']
      chapterType = formChapter.cleaned_data['chapterType']
      name = formChapter.cleaned_data['nameChapter']
      chapterFile = formChapter.cleaned_data['mFile']

      sentChapter = True
      formChapter.save()

  else:
    formLanguage = LanguageForm()
    formType = TypeForm()
    formChapter = ChapterForm()

  return render(request, 'home.html', locals())
