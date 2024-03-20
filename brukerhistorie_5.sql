SELECT
    Teaterstykke.TeaterstykkeNavn AS Teaterstykke,
    Skuespiller.SkuespillerNavn AS Skuespiller,
    Rolle.RolleNavn AS Rolle
FROM
    SkuespillerRolle
JOIN 
    Skuespiller ON SkuespillerRolle.SkuespillerID = Skuespiller.SkuespillerID
JOIN 
    Rolle ON SkuespillerRolle.RolleID = Rolle.RolleID
JOIN 
    RolleStykke ON SkuespillerRolle.RolleID = RolleStykke.RolleID
JOIN 
    Teaterstykke ON RolleStykke.TeaterstykkeNavn = Teaterstykke.TeaterstykkeNavn;

