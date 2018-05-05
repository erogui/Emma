# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import sqlite3 as sq

conn = sq.connect('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db')

cursor = conn.cursor()

a =()
len(a)
conn.commit()

cursor = conn.cursor()
cursor.execute("""
DROP TABLE companies
""")
conn.commit()

cursor.execute("""
DROP TABLE bilans
""")
conn.commit()

import sqlite3 as sq
conn = sq.connect('C:/Users/Guillaume/Documents/guillaume/depot_git/generation_ml/emma.db')

cursor = conn.cursor()
cursor.execute("""
DROP TABLE 
""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS codes_greffe(
                    ticker TEXT,
                    name TEXT
                    )""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS codes_saisie(
                    ticker TEXT,
                    name TEXT
                    )""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS codes_type_bilan(
                    ticker TEXT,
                    name TEXT
                    )""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS codes_confidentialite(
                    ticker TEXT,
                    name TEXT
                    )""")
conn.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS codes_activite(
                    ticker TEXT,
                    name TEXT
                    )""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS companies(
                    siren TEXT PRIMARY KEY UNIQUE,
                    denomination TEXT,
                    adresse TEXT,
                    code_activite TEXT
                    )""")
conn.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS bilans(
                    num_bilan INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    siren TEXT,
                    date_cloture_exercice TEXT,
                    date_cloture_exercice_last TEXT,
                    dure_exercice TEXT,
                    dure_exercice_last TEXT,
                    code_motif TEXT,
                    code_type_bilan TEXT,
                    code_confidentialite TEXT,
                    code_origine_devise TEXT,
                    code_greffe TEXT,
                    num_depot TEXT,
                    num_gestion TEXT,
                    code_devise TEXT,
                    date_depot TEXT,
                    FOREIGN KEY(siren) REFERENCES companies(siren)
                    
                    )""")
conn.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS pages(
                    num_page INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    num_bilan INT,
                    page TEXT,
                    code_liasse TEXT,
                    m1 TEXT,
                    m2 TEXT,
                    m3 TEXT,
                    m4 TEXT,
                    FOREIGN KEY(num_bilan) REFERENCES bilans(num_bilan)
                    
                    )""")
conn.commit()

conn.close()

