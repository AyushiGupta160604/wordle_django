from django.urls import path

from . import views


# urlpatterns = [
#     path("", views.index, name="index"),
# ]

app_name = 'wordle_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('make_guess/', views.make_guess, name='make_guess'),
]
