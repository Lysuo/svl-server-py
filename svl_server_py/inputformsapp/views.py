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

    print "before if/else"
    if request.is_ajax():
      print "ajax!"
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
        sentChapter = True
        formChapterUpdate.save()

  # GET request
  else:
    formLanguage = LanguageForm()
    formType = TypeForm()
    formChapter = ChapterForm()
    formChapterUpdate = UpdateChapterForm()

  return render(request, 'home.html', locals())

@csrf_exempt
def dealAjax(request):
  if request.method == 'POST' and request.is_ajax():
    data = request.POST
    selectedid = data['selected-id'] 
    value = data['value']
    print selectedid
    print value

    if selectedid is "chapterLanguage":
      t = Type.objects.filter(typeLanguage=value)
      print t
    elif selectedid is "chapterLanguageUpdate":
      t = Type.objects.filter(typeLanguage=value)
      print t
    elif selectedid is "chapterTypeUpdate":
      c = Chapter.objects.filter(chapterType=value)
      print c
   
    response_data={}
    response_data['title'] = 'Hola'

#    try:
#      response_data['title']='Hey its done ajax'
#      response_data['message']=sentence

#    except:
#      response_data['title']='NO'
#      response_data['message']='NO'

#    print response_data
    return response_data
  else:
    return HttpResponse("get response")
