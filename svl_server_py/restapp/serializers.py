from inputformsapp.models import Language, Type, Chapter, Word
from rest_framework import serializers
import datetime

class LanguageSerializer(serializers.ModelSerializer):
  mIdL = serializers.CharField(source="id", required=False)
  mName = serializers.CharField(source="nameLanguage")
  mIcon = serializers.CharField(source="icon")

  class Meta:
    model = Language
    fields = ('mIdL', 'mName', 'mIcon')

class TypeSerializer(serializers.ModelSerializer):
  mIdL = serializers.CharField(source="typeLanguage_id")
  mIdT = serializers.CharField(source="id", required=False)
  mName = serializers.CharField(source="nameType")

  class Meta:
    model = Type 
    fields = ('mIdT', 'mIdL', 'mName')

class ChapterSerializer(serializers.ModelSerializer):
  mIdC = serializers.CharField(source="id", required=False)
  mIdL = serializers.CharField(source="chapterLanguage_id", required=False)
  mIdT = serializers.CharField(source="chapterType_id")
  mTitle = serializers.CharField(source="nameChapter")
  mLastUpdate = serializers.CharField(source="mLU", required=False)
  mDateLastUpdate = serializers.DateTimeField(format='%Y/%m/%d at %H:%M', source="mDLU", required=False)
  mDL = serializers.CharField(source="mDl", required=False)

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

  class Meta:
    model = Chapter 
    fields = ('mIdC', 'mIdL', 'mIdT', 'mTitle', 'mDateLastUpdate', 'mLastUpdate', 'mDL')

class WordSerializer(serializers.ModelSerializer):
  mIdL = serializers.CharField(source="wordLanguage_id", required=False, write_only=True)
  mIdT = serializers.CharField(source="wordType_id", required=False, write_only=True)
  mIdC = serializers.CharField(source="wordChapter_id")
  mIdW = serializers.CharField(source="id", required=False)
  mFrenchV = serializers.CharField(source="french")
  mTranslation = serializers.CharField(source="translation")

  class Meta:
    model = Word 
    fields = ('mIdL', 'mIdT', 'mIdW', 'mFrenchV', 'mTranslation', 'mIdC', 'mSuccess', 'mSeen', 'mProp')
