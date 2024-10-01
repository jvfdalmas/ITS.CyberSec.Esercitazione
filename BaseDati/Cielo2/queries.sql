-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:



############################################################

-- 1. Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?

select a.codice, a.nome, count(c.nome) as num_compagnie
from aeroporto a, compagnia c, arrPart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice;

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

select a.codice, count(v.codice) as num_aeroplani
from aeroporto a, Volo v , arrPart ap
where a.codice = 'HTR' and (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.codice = v.codice and v.durataMinuti > 100
group by a.codice;

 codice | num_aeroplani 
--------+---------------
 HTR    |             1
(1 row)


############################################################

-- 3. Quanti sono gli aeroporti sui quali opera la compagnia ‘Apitalia’, per ogni nazione nella quale opera?

select l.nazione, count(l.aeroporto) as num_aeroporti
from luogoAeroporto l, arrPart ap, compagnia c
where (l.aeroporto = ap.arrivo or l.aeroporto = ap.partenza) and ap.comp = c.nome and c.nome = 'Apitalia'
group by l.nazione;

    nazione     | num_aeroporti 
----------------+---------------
 Italy          |             6
 United Kingdom |             1
 USA            |             3
(3 rows)


############################################################

-- 4. Qual è la media, il massimo e il minimo della durata dei voli effettuati dalla compagnia ‘MagicFly’ ?

select cast(avg(v.durataMinuti) as decimal(10,2)) as media, max(v.durataMinuti) as massimo, min(v.durataMinuti) as minimo
from volo v, compagnia c
where v.comp = c.nome and c.nome = 'MagicFly';

 media  | massimo | minimo 
--------+---------+--------
 420.00 |     600 |     60
(1 row)

############################################################

-- 5. Qual è l’anno di fondazione della compagnia più vecchia che opera in ognuno degli aeroporti?

select a.codice, a.nome, min(c.annoFondaz)
from aeroporto a, arrPart ap, compagnia c
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice;

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

select l.nazione, count(distinct l2.nazione) as raggiungibili
from luogoAeroporto l, luogoAeroporto l2, arrPart ap
where l.aeroporto = ap.arrivo
and ap.partenza = l2.aeroporto
and l.nazione  <> l2.nazione
group by l.nazione;

    nazione     | raggiungibili 
----------------+---------------
 France         |             1
 Italy          |             2
 United Kingdom |             1
 USA            |             1
(4 rows)

############################################################

-- 7. Qual è la durata media dei voli che partono da ognuno degli aeroporti?

select a.codice, a.nome, cast(avg(v.durataMinuti) as decimal(10,2)) as media
from aeroporto a, arrPart ap, volo v
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.codice = v.codice
group by a.codice;

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

select c.nome, sum(v.durataMinuti) as totale
from compagnia c, volo v
where c.nome = v.comp and c.annoFondaz >= 1950
group by c.nome;

   nome    | totale 
-----------+--------
 Caimanair |   1043
 MagicFly  |   1260
(2 rows)


############################################################

-- 9. Quali sono gli aeroporti nei quali operano esattamente due compagnie?

select a.codice, a.nome
from aeroporto a, compagnia c, arrPart ap
where (a.codice = ap.arrivo or a.codice = ap.partenza) and ap.comp = c.nome
group by a.codice
having count(distinct c.nome) = 2;

 codice |                 nome                 
--------+--------------------------------------
 CDG    | Charles de Gaulle, Aeroport de Paris
 CIA    | Aeroporto di Roma Ciampino
(2 rows)

############################################################

-- 10. Quali sono le città con almeno due aeroporti?

select l.citta
from luogoAeroporto l, aeroporto a
where a.codice = l.aeroporto
group by l.citta
having count(a.codice) >= 2;

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
having avg(v.durataMinuti) > 6*60;

   nome   
----------
 Apitalia
 MagicFly
(2 rows)


############################################################

-- 12. Qual è il nome delle compagnie i cui voli hanno tutti una durata maggiore di 100 minuti?

select c.nome
from compagnia c, volo v
where c.nome = v.comp
group by c.nome
having min(v.durataMinuti) > 100;

   nome   
----------
 Apitalia
(1 row)

############################################################