from django.shortcuts import render

from study.models import flashcardSet, flashcard


# Create your views here.
def index(request):
    return render(request, 'index.html')

def InputText(request):
    return render(request, 'InputText.html')

def load(request):
    return render(request, 'load.html')

def NameFlashcards(request):
    return render(request, 'NameFlashcards.html')

def card(request):
    cards=flashcard.objects.all()
    context = {'cards':cards}
    return render(request, 'card.html', context)
def Flashcard(request):
    flashcards=flashcardSet.objects.all()
    context = {"flashcards" : flashcards}
    return render(request,
                  'flashcard.html', context)