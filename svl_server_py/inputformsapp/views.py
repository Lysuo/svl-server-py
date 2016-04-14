from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from datetime import datetime
from inputformsapp.models import Language, Type, Chapter, UpdateChapter, Word
from inputformsapp.forms import LanguageForm, TypeForm, ChapterForm, UpdateChapterForm, WordForm

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import csv
import datetime
import json

# Create your views here.

@csrf_exempt
@login_required
def home(request):

  if request.method == 'POST':

    print request.POST

    if request.is_ajax():
      response_data = dealAjax(request)
      return HttpResponse(json.dumps(response_data),content_type='application/json')

    else:

      formLanguage = LanguageForm(request.POST)
      if not formLanguage.has_changed():
        formLanguage._errors = []

      formType= TypeForm(request.POST)
      if not formType.has_changed():
        formType._errors = []

      formChapter= ChapterForm(request.POST, request.FILES)
      if not formChapter.has_changed():
        formChapter._errors = []

      formChapterUpdate= UpdateChapterForm(request.POST, request.FILES)
      if not formChapterUpdate.has_changed():
        formChapterUpdate._errors = []

      formWord = WordForm(request.POST)
      if not formWord.has_changed():
        formWord._errors = []

      # submitting form for languages
      if formLanguage.is_valid() and formLanguage.has_changed():
        language = formLanguage.cleaned_data['nameLanguage']
        icon = formLanguage.cleaned_data['icon']
        sentLanguage = True
        formLanguage.save()

      # submitting form for types
      elif formType.is_valid() and formType.has_changed():
        language = formType.cleaned_data['typeLanguage']
        name = formType.cleaned_data['nameType']
        sentType = True
        formType.save()

      # submitting form for chapters (new)
      elif formChapter.is_valid() and formChapter.has_changed():

        language = formChapter.cleaned_data['chapterLanguage']
        chapterType = formChapter.cleaned_data['chapterType']
        name = formChapter.cleaned_data['nameChapter']
        chapterFile = formChapter.cleaned_data['mFile']
        formChapter.save()

        # parsing csv to insert words
        reader = csv.reader(chapterFile)
        for row in reader:
          w = Word(wordLanguage=Language.objects.filter(nameLanguage=language)[0], wordType=Type.objects.filter(nameType=chapterType)[0], wordChapter=Chapter.objects.filter(nameChapter=name)[0], french=row[0], translation=row[1])
          w.save()
        sentChapter = True

      # submitting form for chapters (update)
      elif formChapterUpdate.is_valid() and formChapterUpdate.has_changed():

        language = formChapterUpdate.cleaned_data['chapterLanguageUpdate']
        chapterType = formChapterUpdate.cleaned_data['chapterTypeUpdate']
        name = formChapterUpdate.cleaned_data['nameChapterUpdate']
        chapterFile = formChapterUpdate.cleaned_data['mFileUpdate']

        c = Chapter.objects.filter(nameChapter=name)[0]
        c.mDLU = datetime.datetime.now()
        c.save()

        formChapterUpdate.save()

        reader = csv.reader(chapterFile)
        for row in reader:
          w = Word(wordLanguage=Language.objects.filter(nameLanguage=language)[0], wordType=Type.objects.filter(nameType=chapterType)[0], wordChapter=Chapter.objects.filter(nameChapter=name)[0], french=row[0], translation=row[1])
          w.save()

        sentChapterUpdate = True

      # submitting form for words
      elif formWord.is_valid() and formWord.has_changed():

        wordLanguage = formWord.cleaned_data['wordLanguage']
        wordType = formWord.cleaned_data['wordType']
        wordChapter = formWord.cleaned_data['wordChapter']
        french = formWord.cleaned_data['french']
        translation = formWord.cleaned_data['translation']

        c = Chapter.objects.filter(nameChapter=wordChapter)[0]
        c.mDLU = datetime.datetime.now()
        c.save()

        formWord.save()
        insertedWord = True

  # GET request
  else:
    formLanguage = LanguageForm()
    formType = TypeForm()
    formChapter = ChapterForm()
    formChapterUpdate = UpdateChapterForm()
    formWord = WordForm()

  return render(request, 'home.html', locals())

@csrf_exempt
def dealAjax(request):
  data = request.POST
  selectedid = data['selected-id'].encode("utf8")
  value = data['value'].encode("utf8")
  mem = request.session.get('memLan')
  if not mem:
    mem = 'none'

  response_data={}

  if selectedid == "chapterLanguage":
    elem = Type.objects.filter(typeLanguage__nameLanguage=value)
    response_data['idTarget']='#chapterType'
    elems = buildTypesA(elem)
  elif selectedid == "wordLanguage":
    elem = Type.objects.filter(typeLanguage__nameLanguage=value)
    response_data['idTarget']='#wordType'
    elems = buildTypesA(elem)
    mem = value
  elif selectedid == "chapterLanguageUpdate":
    elem = Type.objects.filter(typeLanguage__nameLanguage=value)
    response_data['idTarget']='#chapterTypeUpdate'
    elems = buildTypesA(elem)
    mem = value
  elif selectedid == "chapterTypeUpdate":
    elem = Chapter.objects.filter(chapterType__nameType=value, chapterLanguage__nameLanguage=mem)
    response_data['idTarget']='#chapterUpdate'
    elems = buildChaptersA(elem)
  elif selectedid == "wordType":
    elem = Chapter.objects.filter(chapterType__nameType=value, chapterLanguage__nameLanguage=mem)
    response_data['idTarget']='#wordChapter'
    elems = buildChaptersA(elem)

  response_data['elems'] = elems 
  request.session['memLan'] = mem
  print response_data

  return response_data

def buildTypesA(elem):
  types = []
  for e in elem:
    eE = {}
    eE['Name'] = e.nameType.encode('utf8')
    eE['id'] = e.id
    types.append(eE)
  return types

def buildChaptersA(elem):
  chapters = []
  for e in elem:
    eE = {}
    eE['Name'] = e.nameChapter.encode('utf8')
    eE['id'] = e.id
    chapters.append(eE)
  return chapters 



def angular(request):
  return render(request, 'angular.html', locals())
