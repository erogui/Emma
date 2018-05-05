# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:27:31 2018

@author: Guillaume
"""

import Parser_Compte_Resultat as pcr
import Data_Base_Provider as db
import Company as co

code_activite = '77'
print('%'+code_activite+'%')
#C:\Users\Guillaume\Documents\guillaume\depot_git\generation_ml\test_export_base

path_base = 'C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db'
path_folder = 'C:/Users/Guillaume/Documents/guillaume/publicCopie/Bilans_Donnees_Saisies/historique/2017/02'
#path_folder = 'C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/test_export_base'
res = db.select_company_code_activite(path_base,'47%%')
for a in res:
    print(a)
    print(len(a[3]))

pcr.parser_dosier(path_folder,path_base)


res = db.select_companies(path_base)
print((res[0])[1])
a = co.Company((res[0])[0],(res[0])[1],(res[0])[2],(res[0])[3])
print(a.siren)

res = db.select_bilans_all('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db','005720685')
print((res[0])[2])


res = db.select_pages_all('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db')
print((res[0])[1])

from lxml import etree

fichier = etree.parse('C:/Users/Guillaume/Documents/guillaume/publicCopie/Bilans_Donnees_Saisies/historique/2017/01/PUB_CA_005720685_8002_1957B70068_2016_B2017000339.donnees.xml')
racine = fichier.getroot()
print("salut")
for page in fichier.xpath("xmlns:bilan/xmlns:detail/xmlns:page" , namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'}):
        num_page = page.get('numero')
        print(num_page)
        for code in page.xpath("xmlns:liasse", namespaces={'xmlns': 'fr:inpi:odrncs:bilansSaisisXML'}):
            code_liasse = code.get('code')
            m1 = code.get('m1')
            m2 = code.get('m2')
            m3 = code.get('m3')
            m4 = code.get('m4')
            print(m1)
            print(m2)
            print(m3)
            print(m4)