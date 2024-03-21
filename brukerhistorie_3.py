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
 
ønskede_billetter = 0
ønsket_område = ''
ønsket_rad = 0

running = True
while running:
    print("Velkommen til størst av alt er kjærligheten! ...")
    try:
        ønskede_billetter = 9 # int(input("Antall billetter ordinær (1-9): "))
        ønsket_område = "Galleri" # input("Område (Galleri/Balkong/Parkett): ")
        ønsket_rad = 1 # int(input("Radnummer (1-10): "))
    except:
        print("Ugyldig inndata. Vennligst prøv igjen.")
        continue
    
    tilgjengelige_seter = get_avalible_seats(con, cursor, ønsket_rad, ønsket_område, salnavn, forestillingID)

    if ønskede_billetter > len(tilgjengelige_seter):
        print(f"Det er ikke {ønskede_billetter} ledige seter på rad {ønsket_rad}.")
        continue

    dine_seter = tilgjengelige_seter[0:ønskede_billetter]
    
    print(f"Det koster {pris*ønskede_billetter}kr for {ønskede_billetter} billetter i {ønsket_område} på rad {ønsket_rad}.")
    

    billettkjopID = get_highest_value(con, cursor, 'Billettkjop', 'KjopID' ) + 1
    billettID = get_highest_value(con, cursor, 'Billett', 'BillettID') + 1
    

    #legger til kjøpet i databasen
    kjop1 = [billettkjopID, get_date(), get_time(), 1]
    insert_row(con, 'Billettkjop', kjop1)

    #legger til 9 billetter på kjøpIDen
    for seteID in dine_seter:
        insert_row(con, 'Billett', [billettID, type, pris, billettkjopID, seteID, forestillingID ] )
        billettID += 1

    print(f"Du har kjøpt setene med ID: {dine_seter}")

    running = False 
