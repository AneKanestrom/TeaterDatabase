import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("emptydatabase3.db")
cursor = con.cursor()

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
skuespiller_navn = input("Skriv inn navnet paa onsket skuespiller: ")
skuespillere_i_samme_akt(skuespiller_navn)

cursor.close()
con.close()