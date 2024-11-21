--Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

--1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?


 codice |   comp    
--------+-----------
    132 | MagicFly
    263 | Caimanair
    534 | Apitalia
   1265 | Apitalia
     24 | Apitalia
    134 | MagicFly
    265 | Caimanair
    536 | Apitalia
(8 rows)

############################################################

--2. Quali sono le compagnie che hanno voli che superano le 3 ore?

   comp    
-----------
 Caimanair
 MagicFly
 Apitalia
(3 rows)

############################################################

--3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?

 codice |   comp    
--------+-----------
    263 | Caimanair
    534 | Apitalia
(2 rows)

############################################################

--4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?

   comp    
-----------
 Apitalia
 Caimanair
 MagicFly
(3 rows)

############################################################

--5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?

 codice |   comp    
--------+-----------
    134 | MagicFly
    265 | Caimanair
    536 | Apitalia
(3 rows)

############################################################

--6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

   comp    
-----------
 MagicFly
 Caimanair
 Apitalia
(3 rows)

############################################################

--7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?

   comp    
-----------
 Apitalia
 Caimanair
 MagicFly
(3 rows)


############################################################

--8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?

 codice |            nome             |  citta   
--------+-----------------------------+----------
 JFK    | JFK Airport                 | New York
 FCO    | Aeroporto di Roma Fiumicino | Roma
 HTR    | Heathrow Airport, London    | London


############################################################

--9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.

 codice |   comp    | partenza | arrivo 
--------+-----------+----------+--------
    534 | Apitalia  | CIA      | JFK
    134 | MagicFly  | FCO      | JFK
    265 | Caimanair | FCO      | JFK
    536 | Apitalia  | FCO      | JFK
(4 rows)


############################################################

--10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, scalo e arrivo.


    
  compagnia | codice_volo_1 | aeroporto_partenza | scalo | codice_volo_2 | aeroporto_arrivo 
-----------+---------------+--------------------+-------+---------------+------------------
 Caimanair |           263 | CIA                | FCO   |           265 | JFK
 Apitalia  |          1265 | FCO                | CIA   |           534 | JFK
(2 rows)


############################################################

--11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

   nome    
-----------
 Apitalia
 MagicFly
 Caimanair
(3 rows)

############################################################
