# views.py
from django.shortcuts import render, redirect
from .models import Word, Guess
from datetime import date

def index(request):
    today_word = Word.objects.get(date=date.today())
    guesses = Guess.objects.filter(word=today_word)
    return render(request, 'wordle/index.html', {'word': today_word, 'guesses': guesses})

from django.shortcuts import render
from .models import Word, Guess
from datetime import date

def make_guess(request):
    if request.method == "POST":
        guess_text = request.POST['guess']
        today_word = Word.objects.get(date=date.today())  # Get Word instance, not just word_text

        # Generate feedback
        feedback = []
        for idx, char in enumerate(guess_text):
            if char == today_word.word_text[idx]:         # Correct position
                feedback.append("🟩")
            elif char in today_word.word_text:            # Wrong position but present in word
                feedback.append("🟨")
            else:                                         # Not in word
                feedback.append("⬜")
        
        feedback_str = ''.join(feedback)

        # Save the guess and feedback
        new_guess = Guess(word=today_word, guess_text=guess_text, feedback=feedback_str, attempts=1)
        new_guess.save()
        
        return render(request, 'wordle/result.html', {'guess': new_guess, 'feedback': feedback_str})
    return render(request, 'wordle/make_guess.html')
