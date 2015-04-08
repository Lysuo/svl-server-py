from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from datetime import datetime
from inputformsapp.models import Language, Type, Chapter, UpdateChapter, Word
from inputformsapp.forms import LanguageForm, TypeForm, ChapterForm, UpdateChapterForm

import csv

# Create your views here.

def home(request):
  if request.method == 'POST':
    formLanguage = LanguageForm(request.POST)
    formType= TypeForm(request.POST)
    formChapter= ChapterForm(request.POST, request.FILES)
    formChapterUpdate= UpdateChapterForm(request.POST, request.FILES)

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
      formChapter.save()

      reader = csv.reader(chapterFile)

      for row in reader:
        w = Word(wordChapter=Chapter.objects.filter(nameChapter=name)[0], french=row[0], translation=row[1])
        w.save()

      sentChapter = True

    elif formChapterUpdate.is_valid():

      language = formChapterUpdate.cleaned_data['chapterLanguageUpdate']
      chapterType = formChapterUpdate.cleaned_data['chapterTypeUpdate']
      name = formChapterUpdate.cleaned_data['nameChapterUpdate']
      chapterFile = formChapterUpdate.cleaned_data['mFileUpdate']

      sentChapter = True
      formChapterUpdate.save()

  else:
    formLanguage = LanguageForm()
    formType = TypeForm()
    formChapter = ChapterForm()
    formChapterUpdate = UpdateChapterForm()

  return render(request, 'home.html', locals())
