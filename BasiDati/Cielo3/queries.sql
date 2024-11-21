-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Qual e la durata media, per ogni compagnia, dei voli che partono da un aeroporto situato in Italia?

SELECT v.comp, avg(v.durataMinuti) as durataMedia
FROM Volo v, ArrPart ap, LuogoAeroporto la
WHERE v.codice = ap.codice
    AND v.comp = a.comp
    AND ap.partenza = la.aeroporto
    AND la.nazione = 'Italia'
GROUP BY v.comp

############################################################

-- 2. Quali sono le compagnie che operano voli con durata media maggiore della durata media di tutti i voli?

WITH Stats AS (
    SELECT avg(v.durataMinuti) as durataMedia
    FROM Volo
)
StatsComp AS (SELECT v.)