import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("emptydatabase3.db")
cursor = con.cursor()

#dato = '2024-02-03'
type = 'ordinaer'
pris = 350
salnavn = "Gamle Scene"
forestillingID = 6

#! Har ikke fått testet om denne fungerer
""" dato = '2024-02-03'
cursor.execute("SELECT ForestillingID FROM Forestilling WHERE Dato = ?", (dato,))
forestillingID = cursor.fetchone()[0]
 """
wanted_tickets = 0
wanted_area = ''
wanted_row = 0

running = True
while running:
    print("Velkommen til størst av alt er kjærligheten! ...")
    try:
        wanted_tickets = 9 # int(input("Antall billetter ordinær (1-9): "))
        wanted_area = "Galleri" # input("Område (Galleri/Balkong/Parkett): ")
        wanted_row = 1 # int(input("Radnummer (1-10): "))
    except:
        print("Invalid ikke gyldig. Vær så snill å prøv igjen.")
        continue
    
    avaliable_seats = get_avalible_seats(con, cursor, wanted_row, wanted_area, salnavn, forestillingID)

    if wanted_tickets > len(avaliable_seats):
        print(f"Det er ikke {wanted_tickets} ledige seter på rad {wanted_row}.")
        continue

    your_seats = avaliable_seats[0:wanted_tickets]
    
    print(f"Det koster {pris*wanted_tickets}kr for {wanted_tickets} billetter i {wanted_area} på rad {wanted_row}.")
    

    billettkjopID = get_highest_value(con, cursor, 'Billettkjop', 'KjopID' ) + 1
    billettID = get_highest_value(con, cursor, 'Billett', 'BillettID') + 1
    

    #legger til kjøpet i databasen
    kjop1 = [billettkjopID, get_date(), get_time(), 1]
    insert_row(con, 'Billettkjop', kjop1)

    #legger til 9 billetter på kjøpIDen
    for seatID in your_seats:
        insert_row(con, 'Billett', [billettID, type, pris, billettkjopID, seatID, forestillingID ] )
        billettID += 1

    print(f"Du har kjøpt setene med ID: {your_seats}")

    running = False 
    

    





