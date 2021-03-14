from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
	path('', views.api_root),
	path('base-parse/', views.Parse.as_view(), name='parse'),
]
