from django.shortcuts import render

from inputformsapp.models import Language, Type, Chapter, Word

from restapp.serializers import LanguageSerializer, TypeSerializer, ChapterSerializer, WordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.

class LanguageList(APIView):

  def get(self, request, format=None):
    l = Language.objects.all()
    serializer = LanguageSerializer(l, many=True)
    return Response(serializer.data)

class TypeList(APIView):

  def get(self, request, format=None):
    headerL = request.META.get('HTTP_LANGUAGE')
    t = Type.objects.filter(typeLanguage__id=headerL)
    serializer = TypeSerializer(t, many=True)
    return Response(serializer.data)

class ChapterList(APIView):

  def get(self, request, format=None):
    headerT = request.META.get('HTTP_TYPE')
    c = Chapter.objects.filter(chapterType__id=headerT)
    serializer = ChapterSerializer(c, many=True)
    return Response(serializer.data)

class WordList(APIView):

  def get(self, request, format=None):
    headerC = request.META.get('HTTP_CHAPTER')
    w = Word.objects.filter(wordChapter__id=headerC)
    serializer = WordSerializer(w, many=True)
    return Response(serializer.data)
