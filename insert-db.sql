-- brukerhistorie 1
INSERT INTO Sal VALUES('Hovedscenen', 516)
INSERT INTO Sal VALUES('Gamle Scene', 332)

INSERT INTO Teaterstykke VALUES('Kongsemnene')
INSERT INTO Teaterstykke VALUES('Storst av alt er kjaerligheten')

INSERT INTO Forestilling (ForestillingID, Dato, StartTid, Sesong, SalNavn, TeaterstykkeNavn)
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

INSERT INTO Akt VALUES(1, 'AktEn', 'Kongsemnene')
INSERT INTO Akt VALUES(2, 'AktTo', 'Kongsemnene')
INSERT INTO Akt VALUES(3, 'AktTre', 'Kongsemnene')
INSERT INTO Akt VALUES(4, 'AktFire', 'Kongsemnene')
INSERT INTO Akt VALUES(5, 'AktFem', 'Kongsemnene')
INSERT INTO Akt VALUES(1, NULL, 'Storst av alt er kjaerligheten')


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

