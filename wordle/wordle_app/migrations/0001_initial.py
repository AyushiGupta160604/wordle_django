# Generated by Django 5.1.2 on 2024-10-30 08:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_text', models.CharField(max_length=5, unique=True)),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guess_text', models.CharField(max_length=5)),
                ('attempts', models.PositiveIntegerField()),
                ('date_guessed', models.DateTimeField(auto_now_add=True)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wordle_app.word')),
            ],
        ),
    ]