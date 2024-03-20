import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("db_01.db")
cursor = con.cursor()

#Legger inn RolleAkt(RolleID, AktNr, TeaterstykkeNavn) i tabellen for Hovedscenen

insert_row(con, 'RolleAkt', [1,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [1,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [1,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [1,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [1,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [2,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [2,3, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [3,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [3,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [3,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [3,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [3,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [4,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [4,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [5,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [5,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [5,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [5,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [5,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [6,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [6,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [6,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [7,4, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [8,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [8,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [8,3, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [9,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [9,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [9,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [9,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [9,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [10,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [10,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [10,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [10,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [10,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [11,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [11,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [11,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [11,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [11,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [12,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [12,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [12,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [12,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [12,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [13,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [13,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [13,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [13,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [13,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [14,4, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [15,1, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [15,2, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [15,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [15,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [15,5, 'Kongsemnene'])

insert_row(con, 'RolleAkt', [16,3, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [16,4, 'Kongsemnene'])
insert_row(con, 'RolleAkt', [16,5, 'Kongsemnene'])

#Legger inn RolleAkt(RolleID, AktNr, TeaterstykkeNavn) i tabellen for Gamle Scene

insert_row(con, 'RolleAkt', [17,1, 'Storst av alt er kjaerligheten'])
insert_row(con, 'RolleAkt', [18,1, 'Storst av alt er kjaerligheten'])
insert_row(con, 'RolleAkt', [19,1, 'Storst av alt er kjaerligheten'])
insert_row(con, 'RolleAkt', [20,1, 'Storst av alt er kjaerligheten'])
insert_row(con, 'RolleAkt', [21,1, 'Storst av alt er kjaerligheten'])
insert_row(con, 'RolleAkt', [22,1, 'Storst av alt er kjaerligheten'])
insert_row(con, 'RolleAkt', [23,1, 'Storst av alt er kjaerligheten'])

def skuespillere_i_samme_akt(skuespiller_navn):
    cursor.execute("""
        SELECT DISTINCT ra1.AktNr, ra1.TeaterstykkeNavn 
        FROM Skuespiller s 
        JOIN SkuespillerRolle sr ON s.SkuespillerID = sr.SkuespillerID 
        JOIN RolleAkt ra1 ON sr.RolleID = ra1.RolleID 
        WHERE s.SkuespillerNavn = ?""", (skuespiller_navn,))
    skuespiller_navn_akt = cursor.fetchall() #henter aktene skuespiller_navn deltar i

    for akt in skuespiller_navn_akt:
        akt_nr, teaterstykke_navn = akt #henter ut akt_nr og teaterstykke_navn fra listen vi lagde over
        print(f"\n {skuespiller_navn} har deltatt i Akt {akt_nr} av '{teaterstykke_navn}' sammen med:")

        cursor.execute("""
            SELECT DISTINCT s2.SkuespillerNavn 
            FROM Skuespiller s1
            JOIN SkuespillerRolle sr1 ON s1.SkuespillerID = sr1.SkuespillerID
            JOIN RolleAkt ra1 ON sr1.RolleID = ra1.RolleID
            JOIN RolleAkt ra2 ON ra1.AktNr = ra2.AktNr AND ra1.TeaterstykkeNavn = ra2.TeaterstykkeNavn
            JOIN SkuespillerRolle sr2 ON ra2.RolleID = sr2.RolleID
            JOIN Skuespiller s2 ON sr2.SkuespillerID = s2.SkuespillerID
            WHERE s1.SkuespillerNavn = ? AND ra1.AktNr = ? AND ra1.TeaterstykkeNavn = ? AND s1.SkuespillerID != s2.SkuespillerID
            """, (skuespiller_navn, akt_nr, teaterstykke_navn))
        medskuespillere = cursor.fetchall()
        
        for medskuespiller in medskuespillere: 
                print(f"- {medskuespiller[0]}")

# Kjører funksjonene, og lar bruker velge skuespiller
skuespiller_navn = input("Skriv inn navnet på ønsket skuespiller: ")
skuespillere_i_samme_akt(skuespiller_navn)

cursor.close()
con.close()