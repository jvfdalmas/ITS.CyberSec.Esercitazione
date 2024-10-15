-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Quanti sono gli strutturati di ogni fascia?

SELECT posizione, count(stipendio) as numero
FROM persona
GROUP BY posizione;

      posizione       | numero 
----------------------+--------
 Professore Associato |      8
 Ricercatore          |      7
 Professore Ordinario |      6
(3 rows)

############################################################

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

SELECT count(*) as numero
FROM persona
WHERE stipendio >= 40000;

 numero 
--------
      9
(1 row)

############################################################

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(*)
from progetto
where budget > 50000 and fine < CURRENT_DATE;

 count 
-------
     5
(1 row)

############################################################

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?

select avg(ap.oreDurata) as media, max(ap.oreDurata) as massimo, min(ap.oreDurata) as minimo
from attivitaProgetto ap, progetto p
where ap.progetto = p.id and p.nome = 'Pegasus';

       media        | massimo | minimo 
--------------------+---------+--------
 7.8571428571428571 |       8 |      7
(1 row)

############################################################

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?

select avg(ap.oreDurata) as media, max(ap.oreDurata) as massimo, min(ap.oreDurata) as minimo
from attivitaProgetto ap, progetto p
where ap.progetto = p.id and p.nome = 'Pegasus';

       media        | massimo | minimo 
--------------------+---------+--------
 7.8571428571428571 |       8 |      7
(1 row)

############################################################

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select u.id, u.nome, u.cognome, sum(anp.oreDurata) as ore_didattica
from attivitaNonProgettuale anp, persona u
where anp.tipo = 'Didattica' and anp.persona = u.id
group by u.id;

 id |   nome    | cognome  | ore_didattica 
----+-----------+----------+---------------
  0 | Anna      | Bianchi  |             4
  1 | Mario     | Rossi    |             8
  2 | Barbara   | Burso    |             8
  6 | Consolata | Ferrari  |             7
  8 | Asia      | Giordano |             8
(5 rows)

############################################################

-- 7. Qual è la media, il massimo e il minimo degli stipendi dei ricercatori?

select avg(stipendio) as media, max(stipendio) as massimo, min(stipendio) as minimo
from persona
where posizione = 'Ricercatore';

       media        | massimo | minimo 
--------------------+---------+--------
 40304.271205357145 | 45500.3 |  35500
(1 row)

############################################################

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?

select posizione, avg(stipendio) as media, max(stipendio) as massimo, min(stipendio) as minimo
from persona
group by posizione;       media        | massimo | minimo 
--------------------+---------+--------
 7.8571428571428571 |       8 |      7
(1 row)

 Professo       media        | massimo | minimo 
--------------------+---------+--------
 7.8571428571428571 |       8 |      7
(1 row)
re Associato | 38211.143798828125 | 43500.5 | 29200.1
 Ricercatore          | 40304.271205357145 | 45500.3 |   35500
 Professore Ordinario | 39848.667317708336 | 45200.1 | 36922.1
(3 rows)


############################################################

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select p.id, p.nome, sum(ap.oreDurata) as totale_ore
from progetto p, attivitaProgetto ap, persona u
where ap.persona = u.id and u.nome = 'Ginevra' and u.cognome = 'Riva' and ap.progetto = p.id
group by p.id;

 id |  nome   | totale_ore 
----+---------+------------
  1 | Pegasus |          8
(1 row)


############################################################

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select p.id, p.nome
from progetto p, attivitaProgetto ap, persona u
where ap.persona = u.id and ap.progetto = p.id
group by p.id
having count(u.id)>2;

 id |  nome   
----+---------
  3 | Simap
  1 | Pegasus
(2 rows)

############################################################

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select u.id, u.nome, u.cognome
from persona u, progetto p, attivitaProgetto ap
where ap.persona = u.id and ap.progetto = p.id and posizione = 'Professore Associato'
group by u.id
having count(p.id) > 1;

 id |  nome  | cognome 
----+--------+---------
  4 | Aurora | Bianchi
(1 row)

############################################################
