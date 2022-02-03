from tabnanny import verbose
from django.contrib import admin
from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'advice', 'votes')
    list_filter = ('votes',)
admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)
# Register your models here.
