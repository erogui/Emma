from django.urls import path, include
from . import views
from Companies.models import Identite
from django.views.generic import ListView, DetailView

urlpatterns = [
	path('', views.companies , name='companies'),
	path('<str:code_activite>/<str:code_postale>/<str:siren>/<str:nom>/<int:page>', views.companies , name='companies'),
	path('bilans/<str:siren>', views.bilans, name='bilans'),
	path('bilans/pages/<str:date_cloture_exercice>/<int:num_bilan>/<str:code_type_bilan>', views.pages, name='pages'),
]