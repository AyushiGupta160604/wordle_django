from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("wordle/", include("wordle_app.urls", namespace="wordle")), 
]
