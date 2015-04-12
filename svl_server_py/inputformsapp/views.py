from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404

from datetime import datetime
from inputformsapp.models import Language, Type, Chapter, UpdateChapter, Word
from inputformsapp.forms import LanguageForm, TypeForm, ChapterForm, UpdateChapterForm

from django.views.decorators.csrf import csrf_exempt

import csv
import json

# Create your views here.

@csrf_exempt
def home(request):

  if request.method == 'POST':

    print request.POST

    if request.is_ajax():
      response_data = dealAjax(request)
      return HttpResponse(json.dumps(response_data),content_type='application/json')

    else:
      formLanguage = LanguageForm(request.POST)
      formType= TypeForm(request.POST)
      formChapter= ChapterForm(request.POST, request.FILES)
      formChapterUpdate= UpdateChapterForm(request.POST, request.FILES)


      # submitting form for languages
      if formLanguage.is_valid():
        language = formLanguage.cleaned_data['nameLanguage']
        icon = formLanguage.cleaned_data['icon']
        sentLanguage = True
        formLanguage.save()


      # submitting form for types
      elif formType.is_valid():
        language = formType.cleaned_data['typeLanguage']
        name = formType.cleaned_data['nameType']
        sentType = True
        formType.save()

      # submitting form for chapters (new)
      elif formChapter.is_valid():

        language = formChapter.cleaned_data['chapterLanguage']
        chapterType = formChapter.cleaned_data['chapterType']
        name = formChapter.cleaned_data['nameChapter']
        chapterFile = formChapter.cleaned_data['mFile']
        formChapter.save()

        # parsing csv to insert words
        reader = csv.reader(chapterFile)
        for row in reader:
          w = Word(wordChapter=Chapter.objects.filter(nameChapter=name)[0], french=row[0], translation=row[1])
          w.save()
        sentChapter = True

      # submitting form for chapters (update)
      elif formChapterUpdate.is_valid():

        language = formChapterUpdate.cleaned_data['chapterLanguageUpdate']
        chapterType = formChapterUpdate.cleaned_data['chapterTypeUpdate']
        name = formChapterUpdate.cleaned_data['nameChapterUpdate']
        chapterFile = formChapterUpdate.cleaned_data['mFileUpdate']
        formChapterUpdate.save()

        reader = csv.reader(chapterFile)
        for row in reader:
          w = Word(wordChapter=Chapter.objects.filter(nameChapter=name)[0], french=row[0], translation=row[1])
          w.save()

        sentChapterUpdate = True

  # GET request
  else:
    formLanguage = LanguageForm()
    formType = TypeForm()
    formChapter = ChapterForm()
    formChapterUpdate = UpdateChapterForm()

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
  elif selectedid == "chapterLanguageUpdate":
    elem = Type.objects.filter(typeLanguage__nameLanguage=value)
    response_data['idTarget']='#chapterTypeUpdate'
    elems = buildTypesA(elem)
    mem = value
  elif selectedid == "chapterTypeUpdate":
    elem = Chapter.objects.filter(chapterType__nameType=value, chapterLanguage__nameLanguage=mem)
    response_data['idTarget']='#chapterUpdate'
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
