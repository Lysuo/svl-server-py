from django.contrib import admin
from inputformsapp.models import Type, Language, Chapter, Word, UpdateChapter
from restapp.models import InfosChapter, InfosWord

# Register your models here.

class InfosChapterAdmin(admin.ModelAdmin):
  list_display = ('id', 'mUser', 'mTitle', 'isInProgress', 'mLastCompleted',)
  list_filter = ('mUser', 'isInProgress',)
  ordering = ('id',)

class InfosWordAdmin(admin.ModelAdmin):
  list_display = ('id', 'mUser', 'mTitle', 'mPropStat', 'mLastRevisionTS',)
  list_filter = ('mUser', 'mTitle',)
  ordering = ('id',)

admin.site.register(InfosChapter, InfosChapterAdmin)
admin.site.register(InfosWord, InfosWordAdmin)
