from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from django.db.models import Q

# Create your views here.
@api_view(["GET","POST"])
def notes(request):
    if request.method == "GET":
        query = request.query_params.get('search')
        category = request.query_params.get('cat')
        notes = Note.objects.all()
       
        if category and category != "ALL":
            notes = notes.filter(category__iexact=category)
        if query:
            notes = notes.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query))
       
        noteSerializers = NoteSerializer(notes,many=True).data
        return Response(noteSerializers)
    elif request.method == "POST":
        data = request.data
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT","DELETE","GET"])
def note_details(request,slug):
    try:
        note = Note.objects.get(slug=slug)
    except Note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "GET":
         serializer = NoteSerializer(note).data
         return Response(serializer)
    elif request.method == "PUT":
        data =request.data
        serializer = NoteSerializer(note,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
