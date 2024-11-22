--Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

--1. Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?

select distinct v.comp, v.codice
from volo v
where v.durataMinuti >= 180;

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

select distinct v.comp
from volo v
where v.durataMinuti > 180;

   comp    
-----------
 Caimanair
 MagicFly
 Apitalia
(3 rows)

############################################################

--3. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto con codice ‘CIA’ ?

select codice, comp 
from arrpart 
where partenza = 'CIA';

 codice |   comp    
--------+-----------
    263 | Caimanair
    534 | Apitalia
(2 rows)

############################################################

--4. Quali sono le compagnie che hanno voli che arrivano all’aeroporto con codice ‘FCO’ ?

select distinct comp 
from arrpart 
where arrivo = 'FCO';

   comp    
-----------
 Apitalia
 Caimanair
 MagicFly
(3 rows)

############################################################

--5. Quali sono i voli (codice e nome della compagnia) che partono dall’aeroporto ‘FCO’ e arrivano all’aeroporto ‘JFK’ ?

select codice, comp 
from arrpart 
where arrivo = 'JFK' 
   and partenza = 'FCO';

 codice |   comp    
--------+-----------
    134 | MagicFly
    265 | Caimanair
    536 | Apitalia
(3 rows)

############################################################

--6. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’ e atterrano all’aeroporto ‘JFK’ ?

select distinct comp 
from arrpart 
where arrivo = 'JFK' and partenza = 'FCO';

   comp    
-----------
 MagicFly
 Caimanair
 Apitalia
(3 rows)

############################################################

--7. Quali sono i nomi delle compagnie che hanno voli diretti dalla città di ‘Roma’ alla città di ‘New York’ ?

select distinct comp 
from arrpart 
where arrivo in (select aeroporto from LuogoAeroporto where citta = 'New York') 
   and partenza in (select aeroporto from LuogoAeroporto where citta = 'Roma');


   comp    
-----------
 Apitalia
 Caimanair
 MagicFly
(3 rows)


############################################################

--8. Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali partono voli della compagnia di nome ‘MagicFly’ ?

select a.codice, a.nome, la.citta
from aeroporto a
JOIN luogoaeroporto la on la.aeroporto = a.codice
JOIN arrpart ap on la.aeroporto = ap.partenza
Where ap.comp = 'MagicFly';

-- alternativa
select a.codice, a.nome, la.citta
from aeroporto a, luogoaeroporto la, arrpart ap
Where la.aeroporto = a.codice
	and ap.comp = 'MagicFly'
	and la.aeroporto = ap.partenza;

 codice |            nome             |  citta   
--------+-----------------------------+----------
 JFK    | JFK Airport                 | New York
 FCO    | Aeroporto di Roma Fiumicino | Roma
 HTR    | Heathrow Airport, London    | London


############################################################

--9. Quali sono i voli che partono da un qualunque aeroporto della città di ‘Roma’ e atterrano ad un qualunque aeroporto della città di ‘New York’ ? Restituire: codice del volo, nome della compagnia, e aeroporti di partenza e arrivo.

select v.codice, v.comp, ap.partenza, ap.arrivo
from volo v, arrpart ap 
WHERE v.codice = ap.codice
	and ap.partenza in (select aeroporto from luogoaeroporto where citta = 'Roma')
	and ap.arrivo in (select aeroporto from luogoaeroporto where citta = 'New York');

 codice |   comp    | partenza | arrivo 
--------+-----------+----------+--------
    534 | Apitalia  | CIA      | JFK
    134 | MagicFly  | FCO      | JFK
    265 | Caimanair | FCO      | JFK
    536 | Apitalia  | FCO      | JFK
(4 rows)


############################################################

--10. Quali sono i possibili piani di volo con esattamente un cambio (utilizzando solo voli della stessa compagnia) da un qualunque aeroporto della città di ‘Roma’ ad un qualunque aeroporto della città di ‘New York’ ? Restituire: nome della compagnia, codici dei voli, e aeroporti di partenza, scalo e arrivo.

select distinct v1.comp, v1.codice as codice_volo_1, ap1.partenza as aeroporto_partenza, ap1.arrivo as scalo, v2.codice as codice_volo_2, ap2.arrivo as aeroporto_arrivo
from volo v1, volo v2, arrpart as ap1, arrpart as ap2
where v1.codice = ap1.codice
	and v2.codice = ap2.codice
   and v1.comp = v2.comp
   and ap1.partenza in (select aeroporto from luogoaeroporto where citta = 'Roma')
   and ap1.arrivo <> (select aeroporto from luogoaeroporto where citta = 'New York')
   and ap1.arrivo = ap2.partenza
   and ap2.arrivo in (select aeroporto from luogoaeroporto where citta = 'New York');
    
  compagnia | codice_volo_1 | aeroporto_partenza | scalo | codice_volo_2 | aeroporto_arrivo 
-----------+---------------+--------------------+-------+---------------+------------------
 Caimanair |           263 | CIA                | FCO   |           265 | JFK
 Apitalia  |          1265 | FCO                | CIA   |           534 | JFK
(2 rows)


############################################################

--11. Quali sono le compagnie che hanno voli che partono dall’aeroporto ‘FCO’, atterrano all’aeroporto ‘JFK’, e di cui si conosce l’anno di fondazione?

select distinct c.nome
from compagnia c, arrpart ap  
where c.annofondaz is not null
   and ap.comp = c.nome
   and ap.arrivo = 'JFK';

   nome    
-----------
 Apitalia
 MagicFly
 Caimanair
(3 rows)

############################################################
