# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 11:30:15 2018

@author: Guillaume
"""

class Company:
    
    def __init__(self, siren, denomination, adresse, code_activite):
        """Constructeur de notre classe"""
        self.siren = siren
        self.denomination = denomination
        self.adresse = adresse
        self.code_activite = code_activite
        
        
class Bilan:
    
    def __init__(self, num_bilan, siren ,date_cloture_exercice, 
                 date_cloture_exercice_last, dure_exercice , dure_exercice_last, 
                 code_motif, code_type_bilan, code_confidentialite, code_origine_devise,
                 code_greffe,num_depot,num_gestion,code_devise,date_depot):
        """Constructeur de notre classe"""
        self.num_bilan = num_bilan
        self.siren = siren
        self.date_cloture_exercice = date_cloture_exercice
        self.date_cloture_exercice_last = date_cloture_exercice_last
        self.dure_exercice = dure_exercice
        self.dure_exercice_last = dure_exercice_last
        self.code_motif = code_motif
        self.code_type_bilan = code_type_bilan
        self.code_confidentialite = code_confidentialite
        self.code_origine_devise = code_origine_devise
        self.code_greffe = code_greffe
        self.num_depot = num_depot
        self.num_gestion = num_gestion
        self.code_devise = code_devise
        self.date_depot = date_depot
        
        
class Page:
    
    def __init__(self, num_page, num_bilan, page, code_liasse, m1, m2, m3, m4):
        """Constructeur de notre classe"""
        self.num_page = num_page
        self.num_bilan = num_bilan
        self.page = page
        self.code_liasse = code_liasse
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4