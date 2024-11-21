-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?


 codice |                 nome                 | num_compagnie 
--------+--------------------------------------+---------------
 CIA    | Aeroporto di Roma Ciampino           |             3
 HTR    | Heathrow Airport, London             |             3
 CDG    | Charles de Gaulle, Aeroport de Paris |             2
 FCO    | Aeroporto di Roma Fiumicino          |             8
 JFK    | JFK Airport                          |             6
(5 rows)

############################################################

-- 2. Quanti sono i voli che partono dall’aeroporto ‘HTR’ e hanno una durata di almeno 100 minuti?



 codice | num_aeroplani 
--------+---------------
 HTR    |             1
(1 row)


############################################################

-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?



    nazione     | num_aeroporti 
----------------+---------------
 Italy          |             6
 United Kingdom |             1
 USA            |             3
(3 rows)


############################################################

-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?



 media  | massimo | minimo 
--------+---------+--------
 420.00 |     600 |     60
(1 row)

############################################################

-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?



 codice |                 nome                 | min  
--------+--------------------------------------+------
 CIA    | Aeroporto di Roma Ciampino           | 1900
 HTR    | Heathrow Airport, London             | 1900
 CDG    | Charles de Gaulle, Aeroport de Paris | 1954
 FCO    | Aeroporto di Roma Fiumicino          | 1900
 JFK    | JFK Airport                          | 1900
(5 rows)

############################################################

-- 6. Quante sono le nazioni (diverse) raggiungibili da ogni nazione tramite uno o più voli?



    nazione     | raggiungibili 
----------------+---------------
 France         |             1
 Italy          |             2
 United Kingdom |             1
 USA            |             1
(4 rows)

############################################################

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?



 codice |                 nome                 | media  
--------+--------------------------------------+--------
 CIA    | Aeroporto di Roma Ciampino           | 398.67
 HTR    | Heathrow Airport, London             |  90.00
 CDG    | Charles de Gaulle, Aeroport de Paris |  60.00
 FCO    | Aeroporto di Roma Fiumicino          | 489.13
 JFK    | JFK Airport                          | 571.83
(5 rows)

############################################################

-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?

   nome    | totale 
-----------+--------
 Caimanair |   1043
 MagicFly  |   1260
(2 rows)


############################################################

-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?



 codice |                 nome                 
--------+--------------------------------------
 CDG    | Charles de Gaulle, Aeroport de Paris
 CIA    | Aeroporto di Roma Ciampino
(2 rows)

############################################################

-- 10. Quali sono le città con almeno due aeroporti?



 citta 
-------
 Roma
(1 row)

############################################################

-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?


   comp   
----------
 MagicFly
 Apitalia
(2 rows)

############################################################

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?


   nome   
----------
 Apitalia
(1 row)

############################################################