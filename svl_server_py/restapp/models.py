from django.db import models
from inputformsapp.models import Language, Type, Chapter, Word
from django.contrib.auth.models import User

# Create your models here.

class InfosChapter(models.Model):
  mUser = models.ForeignKey(User)
  mIdC = models.ForeignKey(Chapter)
  mTitle = models.CharField(default='false', max_length=50)
  isInProgress = models.CharField(default='false', max_length=20)
  mLastCompleted = models.CharField(default='false', max_length=50)

  def __unicode__(self):
    return self.mTitle

class InfosWord(models.Model):
  mUser = models.ForeignKey(User)
  mIdC = models.ForeignKey(Chapter)
  mTitle = models.CharField(default='false', max_length=50)
  mIdW = models.ForeignKey(Word)
  mFrench = models.CharField(default='false', max_length=200)
  mFailed = models.IntegerField()
  mSeen = models.IntegerField()
  isBookmarked = models.CharField(default='false', max_length=20)
  mLastRevisionTS = models.CharField(default='false', max_length=50)
  mPropStat = models.FloatField()

  def __unicode__(self):
    return self.mFrench
