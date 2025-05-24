from django.urls import path
from .views import notes ,note_details

urlpatterns = [
    path("notes/",notes,name='notes'),
    path("notes/<slug:slug>",note_details,name='note_details')
]