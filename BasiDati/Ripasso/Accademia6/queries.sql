-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Quanti sono gli strutturati di ogni fascia?

select p.posizione, count(p.posizione)
from persona p
group by p.posizione;

      posizione       | numero 
----------------------+--------
 Professore Associato |      8
 Ricercatore          |      7
 Professore Ordinario |      6
(3 rows)

############################################################

-- 2. Quanti sono gli strutturati con stipendio ≥ 40000?

select count(posizione)
from persona
where stipendio >= 40000;

 numero 
--------
      9
(1 row)

############################################################

-- 3. Quanti sono i progetti già finiti che superano il budget di 50000?

select count(id)
from progetto
where budget > 50000;

 count 
-------
     5
(1 row)

############################################################

-- 4. Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto ‘Pegasus’ ?

select avg(atp.oredurata), max(atp.oredurata), min(atp.oredurata)
from progetto p, attivitaprogetto atp
where p.id = atp.progetto
	and p.nome = 'Pegasus';

-- alternativa:
select avg(atp.oredurata), max(atp.oredurata), min(atp.oredurata)
from progetto p
join attivitaprogetto atp on p.id = atp.progetto
where p.nome = 'Pegasus';

       media        | massimo | minimo 
--------------------+---------+--------
 7.8571428571428571 |       8 |      7
(1 row)

############################################################

-- 5. Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?

select p.id, p.nome, p.cognome, avg(atp.oredurata), max(atp.oredurata), min(atp.oredurata)
from persona p, attivitaprogetto atp, progetto prog
where p.id = atp.persona
	and prog.id = atp.progetto
	and prog.nome = 'Pegasus'
group by p.id, p.nome, p.cognome;

0	"Anna"	"Bianchi"	8.0000000000000000	8	8
2	"Barbara"	"Burso"	7.0000000000000000	7	7
8	"Asia"	"Giordano"	8.0000000000000000	8	8
10	"Ginevra"	"Riva"	8.0000000000000000	8	8

############################################################

-- 6. Qual è il numero totale di ore dedicate alla didattica da ogni docente?

select p.id, p.nome, p.cognome, sum(oredurata)
from persona p
join attivitanonprogettuale atp on atp.persona = p.id
where atp.tipo = 'Didattica'
group by p.id, p.nome, p.cognome;

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

select avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from persona p
where p.posizione = 'Ricercatore';

       media        | massimo | minimo 
--------------------+---------+--------
 40304.271205357145 | 45500.3 |  35500
(1 row)

############################################################

-- 8. Quali sono le medie, i massimi e i minimi degli stipendi dei ricercatori, dei professori associati e dei professori ordinari?

select p.posizione, avg(p.stipendio), max(p.stipendio), min(p.stipendio)
from persona p
group by p.posizione;

############################################################

-- 9. Quante ore ‘Ginevra Riva’ ha dedicato ad ogni progetto nel quale ha lavorato?

select p.nome, p.cognome, prog.nome, sum(atp.oredurata)
from persona p, progetto prog, attivitaprogetto atp
where p.nome = 'Ginevra'
	and p.cognome = 'Riva'
	and p.id = atp.persona
	and prog.nome = 'Pegasus'
group by p.nome, p.cognome, prog.nome;

-- alternativa:
select p.nome, p.cognome, prog.nome, sum(atp.oredurata)
from persona p
join attivitaprogetto atp on atp.persona = p.id
join progetto prog on prog.id = atp.progetto 
where p.nome = 'Ginevra'
	and p.cognome = 'Riva'
	and prog.nome = 'Pegasus'
group by p.nome, p.cognome, prog.nome;

 id |  nome   | totale_ore 
----+---------+------------
  1 | Pegasus |          8
(1 row)

############################################################

-- 10. Qual è il nome dei progetti su cui lavorano più di due strutturati?

select prog.id, prog.nome
from progetto prog 
join attivitaprogetto atp on prog.id = atp.progetto
join persona p on p.id = atp.persona
group by prog.id, prog.nome
having count(atp.persona) > 2;

 id |  nome   
----+---------
  3 | Simap
  1 | Pegasus
(2 rows)

############################################################

-- 11. Quali sono i professori associati che hanno lavorato su più di un progetto?

select p.id, p.nome, p.cognome
from persona p
join attivitaprogetto atp on atp.persona = p.id
where p.posizione = 'Professore Associato'
group by p.id, p.nome, p.cognome
having count(atp.progetto) > 1;

 id |  nome  | cognome 
----+--------+---------
  4 | Aurora | Bianchi
(1 row)

############################################################
