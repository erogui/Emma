from django.shortcuts import render
import Data_Base_Provider as db
from export.forms import ExportForm
# Create your views here.


def export(request,code_activite='',code_postale='',nom ='',siren='',path='',page=1):
	form = ExportForm(request.POST or None)
	liste = []
	code_activite_new = code_activite
	code_postale_new = code_postale
	siren_new = siren
	nom_new = nom
	
	if form.is_valid(): 
		code_activite_new = form.cleaned_data['code_activite']
		code_postale_new = form.cleaned_data['code_postale']
		siren_new = form.cleaned_data['siren']
		nom_new = form.cleaned_data['nom']
		envoi = True
		code_activite_new = code_activite_new+'%%'
		code_postale_new = code_postale_new+'%%'
		siren_new = '%'+siren_new+'%'
		nom_new = '%'+nom_new+'%'
		res = db.select_bilan_pages_company('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',code_activite_new,code_postale_new,siren_new,nom_new)
	
		res.to_csv(path)
	
	
	
	return render(request, 'export/export.html' , {'form':form})
