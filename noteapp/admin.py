from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Note._meta.fields]
admin.site.register(Note,NoteAdmin)
# Register your models here.
