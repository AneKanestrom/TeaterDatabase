-- brukerhistorie 1
INSERT INTO Sal VALUES('Hovedscenen', 516);
INSERT INTO Sal VALUES('Gamle Scene', 332);

INSERT INTO Teaterstykke VALUES('Kongsemnene');
INSERT INTO Teaterstykke VALUES('Storst av alt er kjaerligheten');

INSERT INTO Forestilling(ForestillingsID, Dato, StartTid, Sesong, SalNavn, TeaterstykkeNavn)
VALUES 
    (1, '2024-02-01', '19:00:00', 'vinter/vaarsesongen 2024', 'Hovedscenen', 'Kongsemnene'),
    (2, '2024-02-02', '19:00:00', 'vinter/vaarsesongen 2024', 'Hovedscenen', 'Kongsemnene'),
    (3, '2024-02-03', '19:00:00', 'vinter/vaarsesongen 2024', 'Hovedscenen', 'Kongsemnene'),
    (4, '2024-02-05', '19:00:00', 'vinter/vaarsesongen 2024', 'Hovedscenen', 'Kongsemnene'),
    (5, '2024-02-06', '19:00:00', 'vinter/vaarsesongen 2024', 'Hovedscenen', 'Kongsemnene'),
    (6, '2024-02-03', '18:30:00', 'vinter/vaarsesongen 2024', 'Gamle Scene', 'Storst av alt er kjaerligheten'),
    (7, '2024-02-06', '18:30:00', 'vinter/vaarsesongen 2024', 'Gamle Scene', 'Storst av alt er kjaerligheten'),
    (8, '2024-02-07', '18:30:00', 'vinter/vaarsesongen 2024', 'Gamle Scene', 'Storst av alt er kjaerligheten'),
    (9, '2024-02-12', '18:30:00', 'vinter/vaarsesongen 2024', 'Gamle Scene', 'Storst av alt er kjaerligheten'),
    (10, '2024-02-13', '18:30:00', 'vinter/vaarsesongen 2024', 'Gamle Scene', 'Storst av alt er kjaerligheten'),
    (11, '2024-02-14', '18:30:00', 'vinter/vaarsesongen 2024', 'Gamle Scene', 'Storst av alt er kjaerligheten');

INSERT INTO Akt (AktNr, AktNavn, TeaterstykkeNavn)
VALUES
    (1, 'AktEn', 'Kongsemnene'),
    (2, 'AktTo', 'Kongsemnene'),
    (3, 'AktTre', 'Kongsemnene'),
    (4, 'AktFire', 'Kongsemnene'),
    (5, 'AktFem', 'Kongsemnene'),
    (1, NULL, 'Storst av alt er kjaerligheten');


INSERT INTO Rolle (RolleID, RolleNavn)
VALUES
    (1, 'Haakon Haakonssonn'),
    (2, 'Inga fra Vartjeg'),
    (3, 'Skule Jarl'),
    (4, 'Ragnhild'),
    (5, 'Margrete'),
    (6, 'Sigrid'),
    (7, 'Ingebjorg'),
    (8, 'Biskop Nikolas'),
    (9, 'Gregorius Jonssonn'),
    (10, 'Paal Flida'),
    (11, 'Tronder'),
    (12, 'Baard Bratte'),
    (13, 'Tronder'),
    (14, 'Jatgeir Skald'),
    (15, 'Dagfinn Bonde'),
    (16, 'Peter'),
    (17, 'Sunniva Du Mond Nordal'),
    (18, 'Jo Saberniak'),
    (19, 'Marte M. Steinholt'),
    (20, 'Tor Ivar Hagen'),
    (21, 'Trond-Ove Skrodal'),
    (22, 'Natalie Grondahl Tangen'),
    (23, 'Aasmund Flaten');

INSERT INTO Skuespiller (SkuespillerID, SkuespillerNavn)
VALUES
    (1, 'Arturo Scotti'),
    (2, 'Ingunn Beate Strige Oyen'),
    (3, 'Hans Petter Nilsen'),
    (4, 'Madeleine Brandtzaeg Nilsen'),
    (5, 'Synnove Fossum Eriksen'),
    (6, 'Emma Caroline Deichmann'),
    (7, 'Thomas Jensen Takyi'),
    (8, 'Per Bogstad Gulliksen'),
    (9, 'Isak Holmen Sorensen'),
    (10, 'Fabian Heidelberg Lunde'),
    (11, 'Emil Olafsson'),
    (12, 'Snorre Ryen Tondel'),
    (13, 'Sunniva Du Mond Nordal'),
    (14, 'Jo Saberniak'),
    (15, 'Marte M. Steinholt'),
    (16, 'Tor Ivar Hagen'),
    (17, 'Trond-Ove Skrodal'),
    (18, 'Natalie Grondahl Tangen'),
    (19, 'Aasmund Flaten');

INSERT INTO Ansatt (AnsattID, AnsattNavn, Epost, Ansattstatus, Oppgave)
VALUES
    (1, 'Yury Butusov', 'butusov@trondelagteater.no', 'Fast', 'Regi'),
    (2, 'Yury Butusov', 'butusov@trondelagteater.no', 'Fast', 'Musikkutvelgelse'),
    (3, 'Aleksandr Shishkin-Hokusai', 'shishkinhokusai@trondelagteater.no', 'Midlertidig', 'Scenografi'),
    (4, 'Aleksandr Shishkin-Hokusai', 'shishkinhokusai@trondelagteater.no', 'Innleid', 'Kostymer'),
    (5, 'Eivind Myren', 'myren@trondelagteater.no', 'Fast', 'Lysdesign'),
    (6, 'Mina Rype Stokke', 'stokke@trondelagteater.no', 'Midlertidig', 'Dramaturg'),
    (7, 'Jonas Corell Petersen', 'petersen@trondelagteater.no', 'Fast', 'Regi'),
    (8, 'David Gehrt', 'gehrt@trondelagteater.no', 'Midlertidig', 'Scenografi'),
    (9, 'David Gehrt', 'gehrt@trondelagteater.no', 'Innleid', 'Kostymer'),
    (10, 'Gaute Tonder', 'tonder@trondelagteater.no', 'Fast', 'Musikalsk ansvarlig'),
    (11, 'Magnus Mikaelsen', 'mikaelsen@trondelagteater.no', 'Fast', 'Lysdesign'),
    (12, 'Kristoffer Spender', 'spender@trondelagteater.no', 'Midlertidig', 'Dramaturg');

----
INSERT INTO RolleStykke (RolleID, TeaterstykkeNavn)
VALUES
    (1, 'Kongsemnene'),
    (2, 'Kongsemnene'),
    (3, 'Kongsemnene'),
    (4, 'Kongsemnene'),
    (5, 'Kongsemnene'),
    (6, 'Kongsemnene'),
    (7, 'Kongsemnene'),
    (8, 'Kongsemnene'),
    (9, 'Kongsemnene'),
    (10, 'Kongsemnene'),
    (11, 'Kongsemnene'),
    (12, 'Kongsemnene'),
    (13, 'Kongsemnene'),
    (14, 'Kongsemnene'),
    (15, 'Kongsemnene'),
    (16, 'Kongsemnene'),
    (17, 'Storst av alt er kjaerligheten'),
    (18, 'Storst av alt er kjaerligheten'),
    (19, 'Storst av alt er kjaerligheten'),
    (20, 'Storst av alt er kjaerligheten'),
    (21, 'Storst av alt er kjaerligheten'),
    (22, 'Storst av alt er kjaerligheten'),
    (23, 'Storst av alt er kjaerligheten');

INSERT INTO SkuespillerRolle (SkuespillerID, RolleID, Dato)
VALUES
    (1, 1, '2024-02-03'),
    (2, 2, '2024-02-03'),
    (3, 3, '2024-02-03'),
    (4, 4, '2024-02-03'),
    (5, 5, '2024-02-03'),
    (6, 6, '2024-02-03'),
    (6, 7, '2024-02-03'),
    (7, 8, '2024-02-03'),
    (8, 9, '2024-02-03'),
    (9, 10, '2024-02-03'),
    (9, 11, '2024-02-03'),
    (10, 12, '2024-02-03'),
    (10, 13, '2024-02-03'),
    (11, 14, '2024-02-03'),
    (11, 15, '2024-02-03'),
    (12, 16, '2024-02-03'),
    (13, 17, '2024-02-03'),
    (14, 18, '2024-02-03'),
    (15, 19, '2024-02-03'),
    (16, 20, '2024-02-03'),
    (17, 21, '2024-02-03'),
    (18, 22, '2024-02-03'),
    (19, 23, '2024-02-03');


---
INSERT INTO RolleAkt (RolleID, AktNr, TeaterstykkeNavn)
VALUES
    (1, 1, 'Kongsemnene'),
    (1, 2, 'Kongsemnene'),
    (1, 3, 'Kongsemnene'),
    (1, 4, 'Kongsemnene'),
    (1, 5, 'Kongsemnene'),
    (2, 1, 'Kongsemnene'),
    (2, 3, 'Kongsemnene'),
    (3, 1, 'Kongsemnene'),
    (3, 2, 'Kongsemnene'),
    (3, 3, 'Kongsemnene'),
    (3, 4, 'Kongsemnene'),
    (3, 5, 'Kongsemnene'),
    (4, 1, 'Kongsemnene'),
    (4, 5, 'Kongsemnene'),
    (5, 1, 'Kongsemnene'),
    (5, 2, 'Kongsemnene'),
    (5, 3, 'Kongsemnene'),
    (5, 4, 'Kongsemnene'),
    (5, 5, 'Kongsemnene'),
    (6, 1, 'Kongsemnene'),
    (6, 2, 'Kongsemnene'),
    (6, 5, 'Kongsemnene'),
    (7, 4, 'Kongsemnene'),
    (8, 1, 'Kongsemnene'),
    (8, 2, 'Kongsemnene'),
    (8, 3, 'Kongsemnene'),
    (9, 1, 'Kongsemnene'),
    (9, 2, 'Kongsemnene'),
    (9, 3, 'Kongsemnene'),
    (9, 4, 'Kongsemnene'),
    (9, 5, 'Kongsemnene'),
    (10, 1, 'Kongsemnene'),
    (10, 2, 'Kongsemnene'),
    (10, 3, 'Kongsemnene'),
    (10, 4, 'Kongsemnene'),
    (10, 5, 'Kongsemnene'),
    (11, 1, 'Kongsemnene'),
    (11, 2, 'Kongsemnene'),
    (11, 3, 'Kongsemnene'),
    (11, 4, 'Kongsemnene'),
    (11, 5, 'Kongsemnene'),
    (12, 1, 'Kongsemnene'),
    (12, 2, 'Kongsemnene'),
    (12, 3, 'Kongsemnene'),
    (12, 4, 'Kongsemnene'),
    (12, 5, 'Kongsemnene'),
    (13, 1, 'Kongsemnene'),
    (13, 2, 'Kongsemnene'),
    (13, 3, 'Kongsemnene'),
    (13, 4, 'Kongsemnene'),
    (13, 5, 'Kongsemnene'),
    (14, 4, 'Kongsemnene'),
    (15, 1, 'Kongsemnene'),
    (15, 2, 'Kongsemnene'),
    (15, 3, 'Kongsemnene'),
    (15, 4, 'Kongsemnene'),
    (15, 5, 'Kongsemnene'),
    (16, 3, 'Kongsemnene'),
    (16, 4, 'Kongsemnene'),
    (16, 5, 'Kongsemnene'),
    (17, 1, 'Storst av alt er kjaerligheten'),
    (18, 1, 'Storst av alt er kjaerligheten'),
    (19, 1, 'Storst av alt er kjaerligheten'),
    (20, 1, 'Storst av alt er kjaerligheten'),
    (21, 1, 'Storst av alt er kjaerligheten'),
    (22, 1, 'Storst av alt er kjaerligheten'),
    (23, 1, 'Storst av alt er kjaerligheten');

