from django.urls import path, include
from . import views
from Companies.models import Identite
from django.views.generic import ListView, DetailView

urlpatterns = [
	path('', views.export , name='export'),
	path('<str:code_activite>/<str:code_postale>/<str:siren>/<str:nom>/<str:path>/<int:page>', views.export , name='export'),
]