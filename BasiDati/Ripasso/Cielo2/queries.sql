-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?

select a.codice, a.nome, count(c.nome) as num_comp
from aeroporto a, compagnia c, arrpart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice, a.nome;

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

select ap.partenza, count(v.durataminuti)
from arrpart ap, volo v
where ap.codice = v.codice
	and v.durataminuti > 100
	and ap.partenza = 'HTR'
group by ap.partenza;

 codice | num_aeroplani 
--------+---------------
 HTR    |             1
(1 row)


############################################################

-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?

select la.nazione, count(distinct aeroporto) as numeroAeroporto
from arrpart ap, luogoaeroporto la
where (ap.partenza = la.aeroporto or ap.arrivo = la.aeroporto) 
	and ap.comp = 'Apitalia'
group by la.nazione;

    nazione     | num_aeroporti 
----------------+---------------
 Italy          |             2
 United Kingdom |             1
 USA            |             1
(3 rows)


############################################################

-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?

select avg(v.durataMinuti), max(v.durataMinuti), min(v.durataMinuti)
from volo v
where comp = 'MagicFly';

 media  | massimo | minimo 
--------+---------+--------
 420.00 |     600 |     60
(1 row)

############################################################

-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?

select a.codice, a.nome, min(c.annoFondaz)
from aeroporto a, compagnia c, arrpart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza)
   and ap.comp = c.nome
group by a.codice, a.nome;


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

select la1.nazione, count(distinct la1.nazione)
from luogoaeroporto la1, luogoaeroporto la2, arrpart ap
where ap.partenza = la1.aeroporto
	and ap.arrivo = la2.aeroporto
	and la1.nazione <> la2.nazione
group by la1.nazione;


    nazione     | raggiungibili 
----------------+---------------
 France         |             1
 Italy          |             2
 United Kingdom |             1
 USA            |             1
(4 rows)

############################################################

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select a.nome, round(avg(v.durataminuti),2)
from aeroporto a, volo v, arrpart ap
where ap.partenza = a.codice
	and v.codice = ap.codice
group by a.nome;

 codice |                 nome                 | media  
--------+--------------------------------------+--------
 CIA    | Aeroporto di Roma Ciampino           | 407.00
 HTR    | Heathrow Airport, London             | 105.00
 CDG    | Charles de Gaulle, Aeroport de Paris |  60.00
 FCO    | Aeroporto di Roma Fiumicino          | 545.50
 JFK    | JFK Airport                          | 599.50
(5 rows)

############################################################

-- 8. Qual è la durata complessiva dei voli operati da ognuna delle compagnie fondate a partire dal 1950?

select c.nome, sum(v.durataminuti)
from compagnia c, volo v
where c.annofondaz > 1950
	and c.nome = v.comp
group by c.nome;

   nome    | totale 
-----------+--------
 Caimanair |   1043
 MagicFly  |   1260
(2 rows)


############################################################

-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.nome
from aeroporto a, arrpart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza)
group by a.nome
having count(distinct ap.comp) = 2;


 codice |                 nome                 
--------+--------------------------------------
 CDG    | Charles de Gaulle, Aeroport de Paris
 CIA    | Aeroporto di Roma Ciampino
(2 rows)

############################################################

-- 10. Quali sono le città con almeno due aeroporti?

select la.citta
from luogoaeroporto la
group by la.citta
having count(la.citta) = 2

 citta 
-------
 Roma
(1 row)

############################################################

-- 11. Qual è il nome delle compagnie i cui voli hanno una durata media maggiore di 6 ore?

select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having avg(v.durataminuti) > 360;

   comp   
----------
 MagicFly
 Apitalia
(2 rows)

############################################################

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?

select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having min(v.durataminuti) > 100;

   nome   
----------
 Apitalia
(1 row)

############################################################