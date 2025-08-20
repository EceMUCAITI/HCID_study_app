from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from study.models import flashcardSet, flashcard
from study.form import FlashcardSetForm


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # if you're not sending CSRF in fetch, but better to use token
def delete_flashcard(request, card_id):
    if request.method == "POST":
        card = get_object_or_404(flashcard, id=card_id)
        card.delete()
        return JsonResponse({"deleted": True})
    return JsonResponse({"deleted": False}, status=400)
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

def toggle_favourite(request, card_id):
    if request.method == "POST":  # only allow POST
        card = get_object_or_404(flashcard, id=card_id)
        card.favourite = not card.favourite
        card.save()
        return JsonResponse({"favourite": card.favourite})


def Flashcard(request):
    flashcards=flashcardSet.objects.all()
    context = {"flashcards" : flashcards}
    return render(request,
                  'flashcard.html', context)