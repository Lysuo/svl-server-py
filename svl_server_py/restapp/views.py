from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from inputformsapp.models import Language, Type, Chapter, Word

from restapp.serializers import LanguageSerializer, TypeSerializer, ChapterSerializer, WordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

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
    t = Type.objects.filter(typeLanguage__id=headerL)
    serializer = TypeSerializer(t, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = TypeSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChapterRest(APIView):

  def get(self, request, format=None):
    headerT = request.META.get('HTTP_TYPE')
    c = Chapter.objects.filter(chapterType__id=headerT)
    serializer = ChapterSerializer(c, many=True)
    return Response(serializer.data)

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
    w = Word.objects.filter(wordChapter__id=headerC)
    serializer = WordSerializer(w, many=True)
    print serializer.data
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = WordSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, format=None):
    print "trying to update"
    headerC = request.META.get('HTTP_WORD')
    w = Word.objects.filter(id=headerC)
    serializer = WordSerializer(w, data = request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, format=None):
    headerC = request.META.get('HTTP_WORD')
    try:
      w = Word.objects.filter(id=headerC)
      w.delete()
      content = {'status': 'deleted'}
      return Response(content, status=status.HTTP_201_CREATED)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)
