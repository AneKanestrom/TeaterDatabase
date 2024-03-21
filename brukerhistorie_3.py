import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("emptydatabase3.db")
cursor = con.cursor()

dato = '2024-02-03'
type = 'ordinær'
pris = 350
salnavn = "Gamle Scene"
forestillingID = 6

#OBS! DENNE ER IKKE TESTET, HVIS DEN PRINTER FORESTILLINGID = 6 KAN DERE SLETTE DEN VARIABELEN
#Henter ut forestillingID
sql = f'''SELECT ForestillingsID 
            FROM Forestilling WHERE Dato = {dato}'''

#kjører sql spørringen
cursor.execute(sql)
#Henter ut resultatet
forestillingID = cursor.fetchall()
 
onskede_billetter = 0
onsket_område = ''
onsket_rad = 0

running = True
while running:
    print("Velkommen til storst av alt er kjærligheten! ...")
    try:
        onskede_billetter = 9 # int(input("Antall billetter ordinær (1-9): "))
        onsket_område = "Galleri" # input("Område (Galleri/Balkong/Parkett): ")
        onsket_rad = 1 # int(input("Radnummer (1-10): "))
    except:
        print("Ugyldig inndata. Vennligst prov igjen.")
        continue
    
    tilgjengelige_seter = hent_ledige_seter(con, cursor, onsket_rad, onsket_område, salnavn, forestillingID)

    if onskede_billetter > len(tilgjengelige_seter):
        print(f"Det er ikke {onskede_billetter} ledige seter på rad {onsket_rad}.")
        continue

    dine_seter = tilgjengelige_seter[0:onskede_billetter]
    
    print(f"Det koster {pris*onskede_billetter}kr for {onskede_billetter} billetter i {onsket_område} på rad {onsket_rad}.")
    

    billettkjopID = hent_hoyeste_verdi(con, cursor, 'Billettkjop', 'KjopID' ) + 1
    billettID = hent_hoyeste_verdi(con, cursor, 'Billett', 'BillettID') + 1
    

    #legger til kjøpet i databasen
    kjop1 = [billettkjopID, hent_tid(), hent_tid(), 1]
    sett_inn_rad(con, 'Billettkjop', kjop1)

    #legger til 9 billetter på kjøpIDen
    for seteID in dine_seter:
        sett_inn_rad(con, 'Billett', [billettID, type, pris, billettkjopID, seteID, forestillingID ] )
        billettID += 1

    print(f"Du har kjopt setene med ID: {dine_seter}")

    running = False 
