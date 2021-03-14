from django.urls import path

from .views import Parse, api_roots

app_name = 'core'

urlpatterns = [
    path('', api_roots, name="api_roots"),
    path('parse/', Parse.as_view(), name="parse")
]
