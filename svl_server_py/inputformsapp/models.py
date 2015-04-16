from django.db import models

# Create your models here.

class Language(models.Model):
  nameLanguage = models.CharField(max_length=100)
  icon = models.CharField(max_length=50)

  def __unicode__(self):
    return self.nameLanguage
 
class Type(models.Model):
  typeLanguage = models.ForeignKey(Language)
  nameType = models.CharField(max_length=100)

  def __unicode__(self):
    return self.nameType

class Chapter(models.Model):
  chapterLanguage = models.ForeignKey(Language)
  chapterType = models.ForeignKey(Type)
  nameChapter = models.CharField(max_length=100)
  mDl = models.CharField(default='false', max_length=20)
  mLU = models.CharField(default='true', max_length=20)
  mDLU = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True)
  mFile = models.FileField(upload_to="media/chapters/")

  def __unicode__(self):
    return self.nameChapter

class UpdateChapter(models.Model):
  chapterLanguageUpdate = models.ForeignKey(Language)
  chapterTypeUpdate = models.ForeignKey(Type)
  nameChapterUpdate = models.ForeignKey(Chapter)
  mFileUpdate = models.FileField(upload_to="media/chapters/")

class Word(models.Model):
  wordLanguage = models.ForeignKey(Language)
  wordType = models.ForeignKey(Type)
  wordChapter = models.ForeignKey(Chapter)
  french = models.CharField(max_length=100)
  translation = models.CharField(max_length=100)
  mSuccess = models.IntegerField(default=0)
  mSeen = models.IntegerField(default=0)
  mProp = models.IntegerField(default=1)

  def __unicode__(self):
    return self.french
