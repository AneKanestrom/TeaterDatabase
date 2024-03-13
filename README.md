# Teater DB 
Noen tips til prosjektet

Det er enklest å lage hele prosjektet for bruk av terminalen til å lage input
til programmet ditt.

Her er et eksempel kjørt på ubuntu. Vi leser inn og kjører skjemaet og
innsetting av initielle data ved hjelp av .read-kommandoen i sqlite3.

sveinbra@mersey:~/fag/tdt4145/2024/prosjekt$ sqlite3 teater.db
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> .read schema.sql
sqlite> .read insert-db.sql
sqlite> .q

Her er vi sensorer avhengig av å få levert en tom database, evt. en beskrivelse av hva databasefilen heter i dokumentet.

For kjøring av Python for innsetting av allerede solgte seter:
sveinbra@mersey:~/fag/tdt4145/2024/prosjekt$ python3 scan-seats-hovedscenen.py hovedscenen.txt
sveinbra@mersey:~/fag/tdt4145/2024/prosjekt$ python3 scan-seats-gamle-scene.py gamle-scene.txt

osv.

Noen Python-tips:

Når du pakker ut en linje fra tekstinput, kan du fjerne newline-merket, ved å gjøre følgende:

	stringlength=len(myline)
        slicedline=myline[stringlength::-1]
        for c in slicedline:

For å lese Dato fra input:

    if "Dato" in myline:
        words = myline.split()
        for word in words:
            if len(word) == 10 and word[4] == "-" and word[7] == "-":
                dato =  word
