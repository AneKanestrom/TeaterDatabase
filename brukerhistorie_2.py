import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("emptydatabase3.db")
cursor = con.cursor()

kundeID = 1
#Legger til en ny kunde
insert_row(con, 'KundeProfil',[kundeID, '12345678', 'Ola Normann', 'kongens gate 1'] )

billettype = 'Ordinaer' 
billettpris = 450
salnavn = 'Hovedscenen'
billettID = 1
forestillingID = 3
billettkjopID = 1

#Legger til billettkjøp for hovedscene
insert_row(con, 'Billettkjop',[billettkjopID, '2024-02-03', '00:00:00', kundeID] )

lines = [] #Liste for å lagre linjer fra filen
with open('hovedscenen.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())

dato = lines[0].split(' ')[1] #Datoen for bestillingen

# Begynner med parketten

omraade = lines[6]
radnr = 1
seteID = 1

# looper fra bakerste rad (rad 1) til rad 18
for line in lines[-1:6:-1]:
    for character in line:
        if character in '01':
            add_seat(con, seteID, seteID, radnr, omraade, salnavn)

        if character == '1':
            book_seat(con, seteID, billettID, billettype, billettpris, billettkjopID, forestillingID)
            billettID += 1
        
        seteID += 1

    radnr += 1


# Etter parketten legger vi til for galleriet

omraade = lines[1]
radnr = 0 # Rad 0 er galleriet

for line in lines[2:6]:
    for character in line:
        if character in '01':
            add_seat(con, seteID, seteID, radnr, omraade, salnavn)

        if character == '1':
            book_seat(con, seteID, billettID, billettype, billettpris, billettkjopID, forestillingID)
            billettID += 1
    
        seteID += 1

billettype = 'Ordinaer' 
billettpris = 350
salnavn = 'Gamle Scene'
forestillingID = 6
billettkjopID = 2

#Legger til billettkjøp for gamle scene
insert_row(con, 'Billettkjop',[billettkjopID, '2024-02-03', '00:00:00', kundeID] )

lines = [] #Liste for å lagre linjer fra filen
with open('gamle-scene.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())

dato = lines[0].split(' ')[1] #Datoen for bestillingen

# Galleriet
omraade = lines[1]
radnr = 3

for line in lines[2:5]:
    seteNummer = 1
    for character in line:
        seteID = seteNummer + radnr*1000 
        if character in '01':
            add_seat(con, seteID, seteNummer, radnr, omraade, salnavn)

        if character == '1':
            book_seat(con, seteID, billettID, billettype, billettpris,  billettkjopID, forestillingID)
            billettID += 1
        
        seteNummer += 1

    radnr -= 1


# Balkong
omraade = lines[5]
radnr = 4

for line in lines[6:9]:
    seteNummer = 1
    for character in line:
        seteID = seteNummer + 1000 * radnr + 100
        if character in '01':
            add_seat(con, seteID, seteNummer, radnr, omraade, salnavn)

        if character == '1':
            book_seat(con, seteID, billettID, billettype, billettpris, billettkjopID, forestillingID)
            billettID += 1
        
        seteNummer += 1

    radnr -= 1


# Parkett
omraade = lines[10]
radnr = 10

for line in lines[11:]:
    seteNummer = 1
    for character in line:
        seteID = seteNummer + 1000 * radnr + 200
        if character in '01':
            add_seat(con, seteID, seteNummer, radnr, omraade, salnavn)

        if character == '1':
            book_seat(con, seteID, billettID, billettype, billettpris, billettkjopID, forestillingID)
            billettID += 1
        
        seteNummer += 1

    radnr -= 1

cursor.close()
con.close()