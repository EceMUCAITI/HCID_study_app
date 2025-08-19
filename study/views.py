from django.shortcuts import render, redirect

from study.models import flashcardSet, flashcard
from study.form import FlashcardSetForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

def InputText(request):
    return render(request, 'InputText.html')
def inputFile(request):
    return render(request, 'inputFile.html')

def load(request):
    return render(request, 'load.html')

def NameFlashcards(request):
    if request.method == "POST":
        form = FlashcardSetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('card')  # or wherever you want after saving
    else:
        form = FlashcardSetForm()
    return render(request, 'NameFlashcards.html', {'form': form})

def card(request):
    cards=flashcard.objects.all()
    context = {'cards':cards}
    return render(request, 'card.html', context)

def saveDeck(request):
    return render(request,"SaveTheDeck.html")

def leaveDeck(request):
    return render(request,"LeaveTheDeck.html")

def InputVoice(request):
    return render(request,"InputVoice.html")


def Flashcard(request):
    flashcards=flashcardSet.objects.all()
    context = {"flashcards" : flashcards}
    return render(request,
                  'flashcard.html', context)