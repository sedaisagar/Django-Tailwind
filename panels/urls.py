from django.urls import path, include

urlpatterns = [
    path("", include("panels.public.urls")),
]
