# from hjelpefunk import * (importerer alle funksjoner i en annen fil)

#sletting av rader

def slett_rad(conn, table, attribute, condition):
    try:
        sql = f'''DELETE FROM {table} WHERE {attribute} = '{condition}' '''
        conn.execute(sql)
        conn.commit()
    except Exception as e:
        print("Feil: ", e)

#sette inn rader
def sett_inn_rad(conn, table, values):
    try:
        placeholders = ', '.join(['?'] * len(values))
        sql = f'''INSERT INTO {table} VALUES ({placeholders})'''
        conn.execute(sql, values)
        conn.commit()
    except Exception as e:
        print("Feil: ", e)

#få nå tid (klokkeslett)
def hent_tid():
    import datetime
    now = datetime.datetime.now()
    return "'"+ now.strftime("%H:%M:%S") + "'"

#få dagens dato
def hent_dato():
    import datetime
    now = datetime.datetime.now()
    return  "'" + now.strftime("%Y-%m-%d") + "'"


def legg_til_sete(con, seteID, seteNummer, radnr, omraade, salnavn):
            sett_inn_rad(con, 'Sete', [seteID, seteNummer, radnr, omraade, salnavn])
            print("Sete med ID: " + str(seteID) + " og radnr: " + str(radnr) + " lagt til")


def reserver_sete(con, seteID, billettID, billettype, billettpris, kjopID, forestillingID):
            sett_inn_rad(con, 'Billett', [billettID, billettype, billettpris, kjopID, seteID, forestillingID])
            print("Billett med ID: " + str(billettID) + " og seteID: "  + str(seteID) + " lagt til")



# finner seteID til alle setene i en rad
def hent_ledige_seter(con, cursor, radNr, omraade, salnavn, forestillingsID):
      
    sql = f'''SELECT Sete.seteID
            FROM Sete
            WHERE Sete.seteID NOT IN 
                (SELECT Billett.seteID FROM Billett 
                WHERE Billett.forestillingsID = {forestillingsID})
            AND Sete.radnr = {radNr} 
            AND Sete.omraade = '{omraade}' 
            AND Sete.salnavn = '{salnavn}' '''
    cursor.execute(sql)
    seter = cursor.fetchall()
    con.commit()

    seter = [sete[0] for sete in seter]
    return seter


#hente høyeste verdi for IDer
def hent_hoyeste_verdi(con, cursor, tabellNavn, attributt):
    
    sql = f'''
        SELECT MAX({attributt})
        FROM {tabellNavn} '''
    
    cursor.execute(sql) 
    result = cursor.fetchall()
    con.commit()
    
    return result[0][0]



