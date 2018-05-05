from django.shortcuts import render
import pandas as pd
from lxml import etree
import os
from datetime import datetime
import Data_Base_Provider as db
import Company as co
from Companies.forms import CompaniesForm
import Codes_liasse as cd 
from django.core.paginator import Paginator,EmptyPage
from Codes_liasse import Code_liasse as cl

	

def bilans(request,siren):
	res = db.select_bilans_all('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',siren)
	liste = []
	for k in range(len(res)):
		a = co.Bilan((res[k])[0],(res[k])[1],(res[k])[2],(res[k])[3],(res[k])[4],(res[k])[5],(res[k])[6],cl.code_type_bilan[(res[k])[7]],cl.code_confidentialite[(res[k])[8]],(res[k])[9],cl.code_greffe[(res[k])[10]],(res[k])[11],(res[k])[12],(res[k])[13],(res[k])[14])
		liste.append(a)
	return render(request, 'Companies/bilans.html' , {"bilans":liste, "siren":siren})
	
def companies(request,code_activite='',code_postale='',nom ='',siren='',page=1):
	form = CompaniesForm(request.POST or None)
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
	res = db.select_company_code_activite('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',code_activite_new,code_postale_new,siren_new,nom_new)
		
	for com in res:
		a = co.Company(com[0],com[1],com[2],com[3])
		liste.append(a)
			
	paginator = Paginator(liste, 10)
	try:
        # La définition de nos URL autorise comme argument « page » uniquement 
        # des entiers, nous n'avons pas à nous soucier de PageNotAnInteger
        
		minis = paginator.page(page)
	except EmptyPage:
        # Nous vérifions toutefois que nous ne dépassons pas la limite de page
        # Par convention, nous renvoyons la dernière page dans ce cas
		minis = paginator.page(paginator.num_pages)
	
	
	return render(request, 'Companies/companies.html' , {"companies":minis, "code_activite":code_activite_new, 'code_postale':code_postale_new,'siren':siren_new,'nom':nom_new, 'form':form})

def pages(request,date_cloture_exercice,num_bilan,code_type_bilan):
	actif =[]
	passif =[]
	CR1 =[]
	CR2 =[]
	immo =[]
	ammo =[]
	provision =[]
	creance =[]
	affectation =[]
	
	if code_type_bilan == 'C':
		res = pages_complet(num_bilan)
		actif = res['actif']
		passif = res['passif']
		CR1 = res['CR1']
		CR2 = res['CR2']
		immo = res['immo']
		ammo = res['ammo']
		provision = res['provision']
		creance = res['creance']
		affectation = res['affectation']
	elif code_type_bilan == 'S':
		res = pages_simplifie(num_bilan)
		actif = res['actif']
		CR = res['CR']
		immo = res['immo']
		ammo = res['ammo']
	elif code_type_bilan == 'K':
		res = pages_consolide(num_bilan)
		actif = res['actif']
		passif = res['passif']
		CR = res['CR']
	elif code_type_bilan == 'B' or code_type_bilan == 'A':
		res = pages_banques(num_bilan)
		actif = res['actif']
	
	return render(request, 'Companies/pages.html' , {'actif':actif ,'passif':passif,'CR1':CR1,'CR2':CR2,'immo':immo,'ammo':ammo,'provision':provision,'creance':creance, 'affectation':affectation, "date":date_cloture_exercice})

	
def pages_complet(num_bilan):
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'01')
	actif = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_actif_complet[page[3]],m1,m2,m3,m4)
		actif.append(a)
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'02')
	passif = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_passif_complet[page[3]],m1,m2,m3,m4)
		passif.append(a)
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'03')
	CR1 = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_CR_complet[page[3]],m1,m2,m3,m4)
		CR1.append(a)
		
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'04')
	
	CR2 = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_CR_complet[page[3]],m1,m2,m3,m4)
		CR2.append(a)
		
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'05')
	
	immo = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_Immo_complet[page[3]],m1,m2,m3,m4)
		immo.append(a)
	
		
		
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'06')
	ammo = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_Ammo_complet[page[3]],m1,m2,m3,m4)
		ammo.append(a)
		
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'07')
	provision = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_Provision_complet[page[3]],m1,m2,m3,m4)
		provision.append(a)
		
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'08')
	creance = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_Provision_complet[page[3]],m1,m2,m3,m4)
		creance.append(a)
		
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'11')
	affectation = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_AffecRes_complet[page[3]],m1,m2,m3,m4)
		affectation.append(a)
	
	return {'actif':actif ,'passif':passif,'CR1':CR1,'CR2':CR2,'immo':immo,'ammo':ammo,'provision':provision,'creance':creance, 'affectation':affectation}
		
def pages_simplifie():
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'01')
	actif = []
	
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_actif_simplifie[page[3]],m1,m2,m3,m4)
		actif.append(a)
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'02')
	CR = []
	
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_actif_simplifie[page[3]],m1,m2,m3,m4)
		CR.append(a)
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'03')
	immo = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_CR_simplifie[page[3]],m1,m2,m3,m4)
		immo.append(a)
		
		
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'04')
	provision = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_imm_amo_simplifie[page[3]],m1,m2,m3,m4)
		provision.append(a)
	
	return {'actif':actif ,'CR':CR,'immo':immo,'provision':provision}
		
def pages_consolide():
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'01')
	actif = []
	
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_actif_consolide[page[3]],m1,m2,m3,m4)
		actif.append(a)
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'02')
	passif = []
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_passif_consolide[page[3]],m1,m2,m3,m4)
		passif.append(a)
	
	
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'03')
	CR1 = []
	
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_CR_consolide[page[3]],m1,m2,m3,m4)
		CR1.append(a)
	
	CR2 = []
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'04')
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_CR_consolide[page[3]],m1,m2,m3,m4)
		CR2.append(a)
		
	return {'actif':actif ,'passif':passif,'CR1':CR1 ,'CR2':CR2}
		
def pages_banques():
	res = db.select_bilan_pages('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db',num_bilan,'01')
	actif = []
	
	for page in res:
		m1=0
		if page[4] is not None:
			m1= float(page[4])
		m2=0
		if page[5] is not None:
			m2= float(page[5])
		m3=0
		if page[6] is not None:
			m3= float(page[6])
		m4=0
		if page[7] is not None:
			m4= float(page[7])
		a = co.Page(page[0],page[1],page[2],cl.code_liasse_CA_banques[page[3]],m1,m2,m3,m4)
		actif.append(a)
		
	return {'actif':actif }
	
def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())

	
