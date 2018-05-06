# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 20:33:21 2018

@author: Guillaume
"""

import sqlite3 as sq
#import pandas as pd

def insert_company(path_base,siren,denomination,adresse,code_activite):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO companies(siren, denomination, adresse, code_activite) VALUES(?, ?,?,?)""", 
                   (siren, denomination,adresse,code_activite))
    conn.commit()
    conn.close()
    
def insert_bilans(path_base,siren ,date_cloture_exercice, date_cloture_exercice_last, dure_exercice , dure_exercice_last, code_motif, code_type_bilan, code_confidentialite, code_origine_devise,code_greffe,num_depot,num_gestion,code_devise,date_depot):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO bilans(siren ,date_cloture_exercice, date_cloture_exercice_last, dure_exercice , dure_exercice_last, code_motif, code_type_bilan, code_confidentialite, code_origine_devise,code_greffe,num_depot,num_gestion,code_devise,date_depot) VALUES(?, ?,?,?,?, ?,?,?,?,?,?,?,?,?)""", 
                   (siren ,date_cloture_exercice, date_cloture_exercice_last, dure_exercice , dure_exercice_last, code_motif, code_type_bilan, code_confidentialite, code_origine_devise,code_greffe,num_depot,num_gestion,code_devise,date_depot))
    conn.commit()
    conn.close() 
    
    
def insert_page(path_base,num_bilan ,page ,code_liasse ,m1 ,m2 ,m3 ,m4):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO pages(num_bilan ,page ,code_liasse ,m1 ,m2 ,m3 ,m4) VALUES(?, ?,?,?,?,?,?)""", 
                   (num_bilan ,page ,code_liasse ,m1 ,m2 ,m3 ,m4))
    conn.commit()
    conn.close()
    
def select_bilans(path_base,siren,date_cloture_exercice):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM bilans WHERE siren=? and date_cloture_exercice=?""", (siren,date_cloture_exercice,))
    res = cursor.fetchone()
    conn.close()
    return res
    

def select_company(path_base,siren):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM companies WHERE siren=?""", (siren,))
    res = cursor.fetchone()
    conn.close()
    return res

def select_company_code_activite(path_base,code_activite,adresse,siren,denomination):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM companies WHERE code_activite LIKE ? and adresse LIKE ? and siren LIKE ? and denomination LIKE ?""", (code_activite,adresse,siren,denomination,))
    res = cursor.fetchall()
    conn.close()
    return res

def select_bilans_all(path_base,siren):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM bilans WHERE siren=?""", (siren,))
    res = cursor.fetchall()
    conn.close()
    return res

def select_pages_all(path_base):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM pages """)
    res = cursor.fetchall()
    conn.close()
    return res

def select_bilan_pages(path_base,num_bilan,page):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM pages WHERE num_bilan=? and page=?""", (num_bilan,page,))
    res = cursor.fetchall()
    conn.close()
    return res

def select_companies(path_base):
    conn = sq.connect(path_base, timeout=15)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM companies """)
    res = cursor.fetchall()
    conn.close()
    return res

def select_bilan_pages_company(path_base,code_activite,adresse,siren,denomination):
    conn = sq.connect(path_base, timeout=15)
    df =0# pd.read_sql("""SELECT * FROM pages a, companies c, bilans b WHERE a.num_bilan=b.num_bilan and b.siren=c.siren and c.code_activite LIKE '{}' and c.adresse LIKE '{}' and b.siren LIKE '{}' and c.denomination LIKE '{}'""".format(code_activite,adresse,siren,denomination),conn)
    conn.close()
    return df