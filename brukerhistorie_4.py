import sqlite3
from hjelpefunk import *  
con = sqlite3.connect("emptydatabase3.db")
cursor = con.cursor()

#Hente ut dato
onsket_dato = input("Skriv inn dato (YYYY-MM-DD): ")

sql = f'''SELECT Forestilling.*, Teaterstykke.TeaterstykkeNavn, COUNT(Billett.BillettID) as AntallBilletter
            FROM Forestilling
            JOIN Teaterstykke
            ON Forestilling.TeaterstykkeNavn = Teaterstykke.TeaterstykkeNavn
            JOIN Billett
            ON Forestilling.ForestillingsID = Billett.ForestillingsID
            WHERE Forestilling.dato = '{onsket_dato}'
            GROUP BY Teaterstykke.TeaterstykkeNavn; '''

#Kjører SQL spørringen
cursor.execute(sql)

#Henter ut resultatet
result = cursor.fetchall()

#selekterer ønsket data
play_result = [result[-2:] for result in result]

#Går gjennom resultatet og printer ut
print(f'For {onsket_dato} er det følgende forestillinger og solgte billetter:')
print('-----------------------------')
for play in play_result:
    print(f'Forestilling: {play[0]}')
    print(f'Antall solgte billetter: {play[1]}')
    print('-----------------------------')

cursor.close()
con.close()