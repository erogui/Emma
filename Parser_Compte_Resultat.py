# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 20:28:45 2018

@author: Guillaume
"""


from lxml import etree
import pandas as pd
import os
import Data_Base_Provider as db


def parse_compte_resultat(path,path_base):
    fichier = etree.parse(path)
    racine = fichier.getroot()
    
    siren = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:siren", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    date_cloture = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:date_cloture_exercice",namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_greffe = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_greffe", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    num_depot = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:num_depot", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    num_gestion = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:num_gestion", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_activite = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_activite", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    date_cloture_exercice_n1 = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:date_cloture_exercice_n-1", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    duree_exercice_n = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:duree_exercice_n", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    duree_exercice_n1 = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:duree_exercice_n-1", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    date_depot = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:date_depot", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_motif = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_motif", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_type_bilan = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_type_bilan", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_devise = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_devise", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_origine_devise = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_origine_devise", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    code_confidentialite = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:code_confidentialite", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    denomination = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:denomination", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    adresse = fichier.findall("xmlns:bilan/xmlns:identite/xmlns:adresse", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'})[0].text
    sir = db.select_company(path_base,siren)
    if(not sir):
        db.insert_company(path_base,siren,denomination,adresse,code_activite)
    bi= db.select_bilans(path_base,siren,date_cloture)
    if(not bi):
        db.insert_bilans(path_base,siren,date_cloture,date_cloture_exercice_n1,duree_exercice_n,duree_exercice_n1,
                     code_motif,code_type_bilan,code_confidentialite,code_origine_devise,code_greffe,
                     num_depot,num_gestion,code_devise,date_depot)
    bilan = db.select_bilans(path_base,siren,date_cloture)
    num_bilan = bilan[0]
    for page in fichier.xpath("xmlns:bilan/xmlns:detail/xmlns:page" , namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'}):
        num_page = page.get('numero')
        for code in page.xpath("xmlns:liasse", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'}):
            code_liasse = code.get('code')
            m1 = code.get('m1')
            m2 = code.get('m2')
            m3 = code.get('m3')
            m4 = code.get('m4')
            db.insert_page(path_base,num_bilan ,num_page ,code_liasse ,m1 ,m2 ,m3 ,m4)


def parser_dosier(path_folder,path_base):
    k=0
    for fichier in os.listdir(path_folder):
        temp_path = path_folder+'/'+fichier
        print("bilan comptable")
        print(k)
        parse_compte_resultat(temp_path,path_base)
        k +=1
