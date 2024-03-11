BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "KundeProfil"(
    "KundeID" INTEGER NOT NULL,
    "Mobilnummer" VARCHAR(15) NOT NULL,
    "KundeNavn" TEXT NOT NULL,
    "Adresse" TEXT NOT NULL,
    PRIMARY KEY("KundeID")
);

CREATE TABLE IF NOT EXISTS "Billettkjop"(
    "KjopID" INTEGER NOT NULL,
    "Dato" DATE NOT NULL,
    "Tid" TIME NOT NULL,
    "KundeID" INTEGER NOT NULL,
    PRIMARY KEY("KjopID"),
    FOREIGN KEY ("KundeID") REFERENCES "KundeProfil"("KundeID") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Sal"(
    "SalNavn" TEXT NOT NULL,
    "Kapasitet" INTEGER NOT NULL,
    PRIMARY KEY("SalNavn")
);

CREATE TABLE IF NOT EXISTS "Sete"(
    "SeteID" INTEGER NOT NULL,
    "SeteNr" INTEGER NOT NULL,
    "RadNr" INTEGER NOT NULL,
    "Omraade" TEXT NOT NULL,
    "SalNavn" TEXT NOT NULL,
    PRIMARY KEY("SeteID"),
    FOREIGN KEY ("SalNavn") REFERENCES "Sal"("SalNavn") ON DELETE CASCADE ON UPDATE CASCADE,
);

CREATE TABLE IF NOT EXISTS "Teaterstykke"(
    "TeaterstykkeNavn" TEXT NOT NULL,
    PRIMARY KEY("TeaterstykkeNavn")
);

CREATE TABLE IF NOT EXISTS "Forestilling"(
    "ForestillingsID" INTEGER NOT NULL,
    "Dato" DATE NOT NULL,
    "StartTid" TIME NOT NULL,
    "Sesong" TEXT NOT NULL,
    "SalNavn" TEXT NOT NULL,
    "TeaterstykkeNavn" TEXT NOT NULL,
    PRIMARY KEY("ForestillingsID"),
    FOREIGN KEY ("SalNavn") REFERENCES "Sal"("SalNavn") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("TeaterstykkeNavn") REFERENCES "Teaterstykke"("TeaterstykkeNavn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Billett"(
    "BillettID" INTEGER NOT NULL,
    "Type" TEXT NOT NULL,
    "Pris" INTEGER NOT NULL,
    "KjopID" INTEGER NOT NULL,
    "SeteID" INTEGER NOT NULL,
    "ForestillingsID" INTEGER NOT NULL,
    PRIMARY KEY("BillettID"),
    FOREIGN KEY ("KjopID") REFERENCES "Billettkjop"("KjopID") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("SeteID") REFERENCES "Sete"("SeteID") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("ForestillingsID") REFERENCES "Forestilling"("ForestillingsID") ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE("Type", "Pris", "ForestillingsID")
);

CREATE TABLE IF NOT EXISTS "Akt"(
    "AktNr" INTEGER NOT NULL,
    "AktNavn" TEXT,
    "TeaterstykkeNavn" TEXT NOT NULL,
    PRIMARY KEY("AktNr"),
    FOREIGN KEY ("TeaterstykkeNavn") REFERENCES "Teaterstykke"("TeaterstykkeNavn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "Ansatt"(
    "AnsattID" INTEGER NOT NULL,
    "AnsattNavn" TEXT NOT NULL,
    "Epost" TEXT NOT NULL,
    "Ansattstatus" TEXT NOT NULL,
    "Oppgave" TEXT NOT NULL,
    PRIMARY KEY("AnsattID")
);

CREATE TABLE IF NOT EXISTS "Rolle"(
    "RolleID" INTEGER NOT NULL,
    "RolleNavn" TEXT NOT NULL,
    PRIMARY KEY("RolleID")
);

CREATE TABLE IF NOT EXISTS "Skuespiller"(
    "SkuespillerID" INTEGER NOT NULL,
    "SkuespillerNavn" TEXT NOT NULL,
    PRIMARY KEY("SkuespillerID")
);

CREATE TABLE IF NOT EXISTS "SkuespillerRolle"(
    "SkuespillerID" INTEGER NOT NULL,
    "RolleID" INTEGER NOT NULL,
    "Dato" DATE NOT NULL,
    PRIMARY KEY ("SkuespillerID", "RolleID"),
    FOREIGN KEY ("SkuespillerID") REFERENCES "Skuespiller"("SkuespillerID") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("RolleID") REFERENCES "Rolle"("RolleID") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "RolleAkt"(
    "RolleID" INTEGER NOT NULL,
    "AktNr" INTEGER NOT NULL,
    "TeaterstykkeNavn" TEXT NOT NULL,
    PRIMARY KEY ("RolleID", "AktNr", "TeaterstykkeNavn"),
    FOREIGN KEY ("RolleID") REFERENCES "Rolle"("RolleID") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("AktNr", "TeaterstykkeNavn") REFERENCES "Akt"("AktNr", "TeaterstykkeNavn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "RolleStykke"(
    "RolleID" INTEGER NOT NULL,
    "TeaterstykkeNavn" TEXT NOT NULL,
    PRIMARY KEY ("RolleID", "TeaterstykkeNavn"),
    FOREIGN KEY ("RolleID") REFERENCES "Rolle"("RolleID") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("TeaterstykkeNavn") REFERENCES "Teaterstykke"("TeaterstykkeNavn") ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS "MedvirkerStykke"(
    "AnsattID" INTEGER NOT NULL,
    "TeaterstykkeNavn" TEXT NOT NULL,
    PRIMARY KEY ("AnsattID", "TeaterstykkeNavn"),
    FOREIGN KEY ("AnsattID") REFERENCES "Ansatt"("AnsattID") ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY ("TeaterstykkeNavn") REFERENCES "Teaterstykke"("TeaterstykkeNavn") ON DELETE CASCADE ON UPDATE CASCADE
);

COMMIT;
