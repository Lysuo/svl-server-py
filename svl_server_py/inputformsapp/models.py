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
  mDl = models.BooleanField(default=False)
  mFile = models.FileField(upload_to="chapters/")

  def __unicode__(self):
    return self.nameChapter

class Word(models.Model):
  wordChapter = models.ForeignKey(Type)
  french = models.CharField(max_length=100)
  translation = models.CharField(max_length=100)

  def __unicode__(self):
    return self.french
