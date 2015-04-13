from inputformsapp.models import Language, Type, Chapter, Word
from rest_framework import serializers
import datetime

class LanguageSerializer(serializers.ModelSerializer):
  mIdL = serializers.CharField(source="id")
  mName = serializers.CharField(source="nameLanguage")
  mIcon = serializers.CharField(source="icon")

  class Meta:
    model = Language
    fields = ('mIdL', 'mName', 'mIcon')

class TypeSerializer(serializers.ModelSerializer):
  mIdL = serializers.CharField(source="typeLanguage.id")
  mIdT = serializers.CharField(source="id")
  mName = serializers.CharField(source="nameType")

  class Meta:
    model = Type 
    fields = ('mIdT', 'mIdL', 'mName')

class ChapterSerializer(serializers.ModelSerializer):
  mIdC = serializers.CharField(source="id")
  mIdL = serializers.CharField(source="chapterLanguage.id")
  mIdT = serializers.CharField(source="chapterType.id")
  mTitle = serializers.CharField(source="nameChapter")
  mLastUpdate = serializers.CharField(source="mLU")
  mDateLastUpdate = serializers.DateTimeField(format='%Y/%m/%d at %H:%M', source="mDLU")
  mDL = serializers.CharField(source="mDl")

  class Meta:
    model = Chapter 
    fields = ('mIdC', 'mIdL', 'mIdT', 'mTitle', 'mDateLastUpdate', 'mLastUpdate', 'mDL')

class WordSerializer(serializers.ModelSerializer):
  mIdC = serializers.CharField(source="wordChapter.id")
  mIdW = serializers.CharField(source="id")
  mFrenchV = serializers.CharField(source="french")
  mTranslation = serializers.CharField(source="translation")

  class Meta:
    model = Word 
    fields = ('mIdW', 'mFrenchV', 'mTranslation', 'mIdC', 'mSuccess', 'mSeen', 'mProp')
