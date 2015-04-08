from django.contrib import admin
from inputformsapp.models import Type, Language, Chapter, Word, UpdateChapter

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
  list_display = ('id', 'nameLanguage',)

class TypeAdmin(admin.ModelAdmin):
  list_display = ('id', 'nameType',)
  list_filter = ('typeLanguage',)
  ordering = ('id',)

class ChapterAdmin(admin.ModelAdmin):
  list_display = ('id', 'nameChapter',)
  list_filter = ('chapterLanguage', 'chapterType',)
  ordering = ('id',)

class WordAdmin(admin.ModelAdmin):
  list_display = ('id', 'french', 'translation',)
  list_filter = ('wordChapter',)
  ordering = ('id',)

admin.site.register(Language, LanguageAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(UpdateChapter)
admin.site.register(Word, WordAdmin)
