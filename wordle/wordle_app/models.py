from django.db import models
from datetime import date

class Word(models.Model):
    word_text = models.CharField(max_length=5)
    date = models.DateField(unique=True)

    class Meta:
        app_label = 'wordle_app'

class Guess(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    guess_text = models.CharField(max_length=5)
    feedback = models.CharField(max_length=5, blank=True)  # feedback per letter (e.g., GYYBG)
    attempts = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.guess_text} on {self.word.date}"
