from django.shortcuts import render, get_object_or_404
from rest_framework.renderers import JSONRenderer
from inputformsapp.models import Language, Type, Chapter, Word
from restapp.models import InfosChapter, InfosWord 

from restapp.serializers import LanguageSerializer, TypeSerializer, ChapterSerializer, WordSerializer, InfosChapterSerializer, InfosChapterGETSerializer, InfosWordGETSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from threading import Thread

# Create your views here.


class LanguageRest(APIView):

  def get(self, request, format=None):
    l = Language.objects.all()
    serializer = LanguageSerializer(l, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    print request.data
    serializer = LanguageSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeRest(APIView):

  def get(self, request, format=None):
    headerL = request.META.get('HTTP_LANGUAGE')
    if headerL.isdigit(): 
      t = Type.objects.filter(typeLanguage__id=headerL)
      serializer = TypeSerializer(t, many=True)
      return Response(serializer.data)
    elif headerL == "all":
      t = Type.objects.all()
      serializer = TypeSerializer(t, many=True)
      return Response(serializer.data)
    else:
      content = {'status': 'missing header LANGUAGE'}
      return Response(content, status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, format=None):
    serializer = TypeSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChapterRest(APIView):

  def get(self, request, format=None):
    headerT = request.META.get('HTTP_TYPE')
    if headerT.isdigit(): 
      c = Chapter.objects.filter(chapterType__id=headerT)
      serializer = ChapterSerializer(c, many=True)
      return Response(serializer.data)
    elif headerT == "all":
      c = Chapter.objects.all()
      serializer = ChapterSerializer(c, many=True)
      return Response(serializer.data)
    else:
      content = {'status': 'missing header TYPE'}
      return Response(content, status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, format=None):
    serializer = ChapterSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WordRest(APIView):

  renderer_classes = (JSONRenderer, )

  def get(self, request, format=None):
    headerC = request.META.get('HTTP_CHAPTER')
    if headerC.isdigit(): 
      w = Word.objects.filter(wordChapter__id=headerC)
      serializer = WordSerializer(w, many=True)
      return Response(serializer.data)
    elif headerC == "all":
      w = Word.objects.all()
      serializer = WordSerializer(w, many=True)
      return Response(serializer.data)
    else:
      content = {'status': 'missing header CHAPTER'}
      return Response(content, status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, format=None):
    serializer = WordSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, format=None):
    headerC = request.META.get('HTTP_WORD')
    try:
      w = get_object_or_404(Word, id=headerC)
      serializer = WordSerializer(w, data = request.data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      print e
      content = {'status': 'error. not updated'}
      return Response(content, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, format=None):
    headerC = request.META.get('HTTP_WORD')
    try:
      w = Word.objects.filter(id=headerC)
      w.delete()
      content = {'status': 'deleted'}
      return Response(content, status=status.HTTP_201_CREATED)
    except:
      print e
      content = {'status': 'error. not deleted'}
      return Response(content, status=status.HTTP_400_BAD_REQUEST)

class DumpRest(APIView):

  renderer_classes = (JSONRenderer, )

  def get(self, request, format=None):
    headerU = request.META.get('HTTP_USER')
    headerT = request.META.get('HTTP_TYPE')
    if headerT == "chapters":
      d = InfosChapter.objects.filter(mUser__id=headerU)
      serializer = InfosChapterGETSerializer(d, many=True)
      return Response(serializer.data)
    elif headerT == "words":
      d = InfosWord.objects.filter(mUser__id=headerU)
      serializer = InfosWordGETSerializer(d, many=True)
      return Response(serializer.data)
    else:
      content = {'status': 'missing header USER or TYPE'}
      return Response(content, status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, format=None):
    serializer = InfosChapterSerializer(many=True, data = request.data)
    if serializer.is_valid():
      t = Thread(target = serializer.save)
      t.daemon = True
      t.start()
      return Response(status=status.HTTP_201_CREATED)
    print serializer.errors
    return Response(status=status.HTTP_400_BAD_REQUEST)
