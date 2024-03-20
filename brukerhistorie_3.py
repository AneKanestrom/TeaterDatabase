import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("db_01.db")
cursor = con.cursor()

#dato = '2024-02-03'
#type = 'ordinaer'
pris = 350
salnavn = "Gamle Scene"
#total_cost = 0
forestillingID = 6

wanted_tickets = 0
wanted_area = ''
wanted_row = 0

running = True
while running:
    print("Velkommen til størst av alt er kjærligheten! ...")
    try:
        wanted_tickets = 9 # int(input("Antall billetter ordinær (1-9): "))
        wanted_area = "Galleri" # input("Område (Galleri/Balkong/Parkett): ")
        wanted_row = 1 # int(input("Radnummer (1-10): ")) velger rad 1
    except:
        print("Invalid input. Please try again.")
        continue

    print(f"Det koster {pris*wanted_tickets}kr for {wanted_tickets} billetter i {wanted_area} på rad {wanted_row}.")
    
    avaliable_seats = get_avalible_seats(con, cursor, wanted_row, wanted_area, salnavn, forestillingID)
    
    print(avaliable_seats)
    #TODO: Legge til setene i biletttkjop og printe bilettene som skal kjøpes!!!!
    
    running = False

cursor.close()
con.close()