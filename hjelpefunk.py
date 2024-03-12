# from hjelpefunk import * (importerer alle funksjoner i en annen fil)

#sletting av rader

def delete_rows(conn, table, attribute, condition):
    try:
        sql = f'''DELETE FROM {table} WHERE {attribute} = '{condition}' '''
        conn.execute(sql)
        conn.commit()
    except Exception as e:
        print("Feil: ", e)

def insert_row(conn, table, values):
    try:
        placeholders = ', '.join(['?'] * len(values))
        sql = f'''INSERT INTO {table} VALUES ({placeholders})'''
        conn.execute(sql, values)
        conn.commit()
    except Exception as e:
        print("Feil: ", e)

