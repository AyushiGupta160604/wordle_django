from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("wordle/", include("wordle_app.urls")),
    path("admin/", admin.site.urls),
]