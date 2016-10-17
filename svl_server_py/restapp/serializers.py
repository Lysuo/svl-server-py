from inputformsapp.models import Language, Type, Chapter, Word
from restapp.models import InfosChapter, InfosWord 
from rest_framework import serializers
from django.contrib.auth.models import User
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
  mIdL = serializers.CharField(source="wordLanguage_id", required=False)
  mIdT = serializers.CharField(source="wordType_id", required=False)
  mIdC = serializers.CharField(source="wordChapter_id")
  mIdW = serializers.CharField(source="id", required=False)
  mFrenchV = serializers.CharField(source="french")
  mTranslation = serializers.CharField(source="translation")

  class Meta:
    model = Word 
    fields = ('mIdL', 'mIdT', 'mIdW', 'mFrenchV', 'mTranslation', 'mIdC')

class InfosWordSerializer(serializers.ModelSerializer):

  class Meta:
    model = InfosWord
    fields = ('mIdW', 'mFailed', 'mSeen', 'isBookmarked', 'mLastRevisionTS', 'mPropStat')

class InfosWordGETSerializer(serializers.ModelSerializer):

  class Meta:
    model = InfosWord
    fields = ('mUser', 'mIdC', 'mIdW', 'mFailed', 'mSeen', 'isBookmarked', 'mLastRevisionTS', 'mPropStat')

class InfosChapterSerializer(serializers.ModelSerializer):
  mWords = InfosWordSerializer(many=True)

  class Meta:
    model = InfosChapter
    fields = ('mUser', 'mIdC', 'mTitle', 'isInProgress', 'mLastCompleted', 'mWords')

  def create(self, validated_data):
    if InfosChapter.objects.filter(mUser=validated_data['mUser'], mIdC=validated_data['mIdC']).count() > 0:
      ic = InfosChapter.objects.get(mUser=validated_data['mUser'], mIdC=validated_data['mIdC'])
      ic.isInProgress = validated_data['isInProgress']
      ic.mLastCompleted = validated_data['mLastCompleted']
    else:
      ic = InfosChapter(mUser=validated_data['mUser'], mIdC=validated_data['mIdC'], mTitle=validated_data['mTitle'], isInProgress=validated_data['isInProgress'], mLastCompleted=validated_data['mLastCompleted'])
    ic.save()

    for item in validated_data['mWords']:
      if InfosWord.objects.filter(mUser=validated_data['mUser'], mIdW=item['mIdW']).count() > 0:
        word = InfosWord.objects.get(mUser=validated_data['mUser'], mIdW=item['mIdW'])
        word.mFailed = item['mFailed']
        word.mSeen = item['mSeen']
        word.isBookmarked = item['isBookmarked']
        word.mLastRevisionTS = item['mLastRevisionTS']
        word.mPropStat = item['mPropStat']
      else:
        word = InfosWord(mUser=validated_data['mUser'], mIdC=validated_data['mIdC'], mTitle=validated_data['mIdC'].nameChapter, mIdW=item['mIdW'], mFrench=item['mIdW'].french, mFailed=item['mFailed'], mSeen=item['mSeen'], isBookmarked=item['isBookmarked'], mLastRevisionTS=item['mLastRevisionTS'], mPropStat=item['mPropStat'])
      word.save()

    return ic

class InfosChapterGETSerializer(serializers.ModelSerializer):

  class Meta:
    model = InfosChapter
    fields = ('mUser', 'mIdC', 'mTitle', 'isInProgress', 'mLastCompleted')
