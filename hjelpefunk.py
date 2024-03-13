# from hjelpefunk import * (importerer alle funksjoner i en annen fil)

#sletting av rader

def delete_rows(conn, table, attribute, condition):
    try:
        sql = f'''DELETE FROM {table} WHERE {attribute} = '{condition}' '''
        conn.execute(sql)
        conn.commit()
    except Exception as e:
        print("Feil: ", e)

#sette inn rader
def insert_row(conn, table, values):
    try:
        placeholders = ', '.join(['?'] * len(values))
        sql = f'''INSERT INTO {table} VALUES ({placeholders})'''
        conn.execute(sql, values)
        conn.commit()
    except Exception as e:
        print("Feil: ", e)

#få nå tid (klokkeslett)
def get_time():
    import datetime
    now = datetime.datetime.now()
    return "'"+ now.strftime("%H:%M:%S") + "'"

#få dagens dato
def get_date():
    import datetime
    now = datetime.datetime.now()
    return  "'" + now.strftime("%Y-%m-%d") + "'"


def add_seat(seteID, radnr, omraade, salnavn):
    # TODO: legge inn sete med samme seteid som setenummer
            #insert_row(con, 'Sete', [seteID, seteID, radnr, omraade, salnavn])
            print("Sete med ID: " + str(seteID) + " og radnr: " + str(radnr) + " lagt til")


def book_seat(seteID, billettID, billettype, billettpris):
    # TODO: legge inn billett, NB pass på rekkefølge av attributtene
            #insert_row(con, 'Billett', [billettID, billettype, billettpris, seteID])
            print("Billett med ID: " + str(billettID) + " og seteID: " + str(seteID) + " lagt til")

