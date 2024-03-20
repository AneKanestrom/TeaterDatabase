SELECT Forestilling.TeaterstykkeNavn, Forestilling.Dato, COUNT(Billett.BillettID) AS AntallSolgtePlasser
    FROM Forestilling 
    JOIN Billett ON Forestilling.ForestillingsID = Billett.ForestillingsID
    GROUP BY Forestilling.TeaterstykkeNavn, Forestilling.Dato
    ORDER BY AntallSolgtePlasser DESC;