SELECT DISTINCT Teaterstykke.TeaterstykkeNavn AS Teaterstykke,
                Skuespiller.SkuespillerNavn AS Skuespiller,
                Rolle.RolleNavn AS Rolle
FROM Teaterstykke
JOIN RolleStykke ON Teaterstykke.TeaterstykkeNavn = RolleStykke.TeaterstykkeNavn
JOIN Rolle ON RolleStykke.RolleID = Rolle.RolleID
JOIN SkuespillerRolle ON Rolle.RolleID = SkuespillerRolle.RolleID
JOIN Skuespiller ON SkuespillerRolle.SkuespillerID = Skuespiller.SkuespillerID;