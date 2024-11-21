-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’ ?

select wp.nome, wp.inizio, wp.fine
from wp, progetto p
where wp.progetto = p.id and p.nome = 'Pegasus';

-- alternativa:
select wp.nome, wp.inizio, wp.fine
from wp
join progetto p on wp.progetto = p.id
where p.nome = 'Pegasus';


 id | nome |   inizio   |    fine    
----+------+------------+------------
  0 | WP1  | 2012-01-01 | 2012-12-31
  1 | WP2  | 2012-01-01 | 2012-12-31
  2 | WP3  | 2013-01-01 | 2013-12-31
(3 rows)

############################################################

-- 2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

select distinct p.nome, p.cognome, p.posizione
from persona p, progetto pr, attivitaprogetto at
where p.id = at.persona and at.progetto = pr.id and pr.nome = 'Pegasus'
order by p.cognome desc;

-- alternativa:
select distinct p.nome, p.cognome, p.posizione
from persona p
join attivitaprogetto at on p.id = at.persona
join progetto pr on at.progetto = pr.id
where  pr.nome = 'Pegasus'
order by p.cognome desc;


 id |  nome   | cognome  |      posizione       
----+---------+----------+----------------------
 10 | Ginevra | Riva     | Professore Ordinario
  8 | Asia    | Giordano | Professore Ordinario
  2 | Barbara | Burso    | Ricercatore
  0 | Anna    | Bianchi  | Ricercatore
(4 rows)

############################################################

-- 3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di una attività nel progetto ‘Pegasus’ ?

select distinct p.nome, p.cognome, p.posizione
from persona p
join attivitaprogetto at on p.id = at.persona
join progetto pr on at.progetto = pr.id
where pr.nome = 'Pegasus'
group by p.nome, p.cognome, p.posizione
having count(at.id) > 1;

-- alternativa:
select distinct p.nome, p.cognome, p.posizione
	from persona p, attivitaprogetto at, progetto pr
where pr.nome = 'Pegasus'
	and at.progetto = pr.id
	and p.id = at.persona
group by p.nome, p.cognome, p.posizione
having count(at.id) > 1;

-- alternativa:
SELECT DISTINCT s.id, s.nome, s.cognome, s.posizione
FROM attivitaprogetto a1, attivitaprogetto a2, persona s, progetto p
WHERE a1.id <> a2.id 
	AND a1.progetto = a2.progetto
	AND a1.persona = a2.persona
	AND a1.persona = s.id
	AND a1.progetto = p.id
	AND p.nome = 'Pegasus';

 id | nome | cognome |  posizione  
----+------+---------+-------------
  0 | Anna | Bianchi | Ricercatore
(1 row)

############################################################

-- 4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto almeno una assenza per malattia?

select distinct p.nome, p.cognome, p.posizione
from persona as p
join assenza as a on p.id = a.persona
where a.tipo = 'Malattia'
	and p.posizione = 'Professore Ordinario';

-- alternativa:
select distinct p.nome, p.cognome, p.posizione
from persona as p, assenza as a 
where a.tipo = 'Malattia'
	and p.posizione = 'Professore Ordinario'
	and p.id = a.persona;

 id |  nome   | cognome  |      posizione       
----+---------+----------+----------------------
  8 | Asia    | Giordano | Professore Ordinario
 10 | Ginevra | Riva     | Professore Ordinario
(2 rows)

############################################################

-- 5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto più di una assenza per malattia?

select p.nome, p.cognome, p.posizione
from persona p
join assenza a on a.persona = p.id
where a.tipo = 'Malattia'
group by p.nome, p.cognome, p.posizione
having count(a.id) > 1;

-- alternativa:
select p.nome, p.cognome, p.posizione
from persona p, assenza a
where persona = p.id 
	and a.tipo = 'Malattia'
group by p.nome, p.cognome, p.posizione
having count(a.id) > 1;

-- alternativa:
select distinct p.nome, p.cognome, p.posizione
from persona p, assenza a1, assenza a2
where a1.id <> a2.id
	and a1.tipo = a2.tipo
	and a1.tipo = 'Malattia'
	and a1.persona = a2.persona
	and a1.persona = p.id;

 id |  nome   | cognome |      posizione       
----+---------+---------+----------------------
 10 | Ginevra | Riva    | Professore Ordinario
(1 row)

############################################################

-- 6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno un impegno per didattica?

select distinct p.nome, p.cognome, p.posizione
from persona p, attivitanonprogettuale at
where at.tipo = 'Didattica'
	and p.posizione = 'Ricercatore'
	and at.persona = p.id;

-- alternativa:
select distinct p.nome, p.cognome, p.posizione
from persona p
join attivitanonprogettuale at on at.persona = p.id
where at.tipo = 'Didattica'
	and p.posizione = 'Ricercatore';

 id |  nome   | cognome |  posizione  
----+---------+---------+-------------
  0 | Anna    | Bianchi | Ricercatore
  1 | Mario   | Rossi   | Ricercatore
  2 | Barbara | Burso   | Ricercatore
(3 rows)

############################################################

-- 7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un impegno per didattica?

select p.nome, p.cognome, p.posizione
from persona p
join attivitanonprogettuale at on at.persona = p.id
where at.tipo = 'Didattica'
	and p.posizione = 'Ricercatore'
group by p.nome, p.cognome, p.posizione
having count(at.id) > 1;

-- alternativa:
select distinct p.nome, p.cognome, p.posizione
from persona p, attivitanonprogettuale at1, attivitanonprogettuale at2
where at1.tipo = 'Didattica'
	and at1.tipo = at2.tipo
	and at1.persona = p.id
	and at1.persona = at2.persona
	and at1.id <> at2.id
	and p.posizione = 'Ricercatore';

      
 id |  nome   | cognome |  posizione  
----+---------+---------+-------------
  2 | Barbara | Burso   | Ricercatore
(1 row)

############################################################

-- 8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia attività progettuali che attività non progettuali?

select distinct p.nome, p.cognome
from persona p
join attivitaprogetto ap on ap.persona = p.id
join attivitanonprogettuale anp on anp.persona = p.id
where ap.giorno = anp.giorno;

-- alternativa:
select distinct p.nome, p.cognome
from persona p, attivitaprogetto ap, attivitanonprogettuale anp 
where ap.giorno = anp.giorno
	and ap.persona = p.id
	and anp.persona = p.id;

 id | nome | cognome 
----+------+---------
  0 | Anna | Bianchi
(1 row)

############################################################

-- 9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia attività progettuali che attività non progettuali? Si richiede anche di proiettare il giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di entrambe le attività.

select distinct p.nome, p.cognome, ap.giorno as giorno, prog.nome as progetto, anp.tipo as attività_non_progettuali, ap.oredurata as AttProg_Durata, anp.oredurata as AttNonProg_Durata
from persona p, attivitaprogetto ap, attivitanonprogettuale anp, progetto prog 
where ap.giorno = anp.giorno
	and ap.persona = p.id
	and anp.persona = p.id
	and prog.id = ap.progetto;

-- alternativa:
select distinct p.nome, p.cognome, ap.giorno as giorno, prog.nome as progetto, anp.tipo as attività_non_progettuali, ap.oredurata as AttProg_Durata, anp.oredurata as AttNonProg_Durata
from persona p 
join attivitaprogetto ap on ap.persona = p.id
join attivitanonprogettuale anp on anp.persona = p.id
join progetto prog on prog.id = ap.progetto
where ap.giorno = anp.giorno;


 id | nome | cognome |   giorno   | nome_progetto | tipo_non_progettuale | ore_progettuali | ore_non_progettuali 
----+------+---------+------------+---------------+----------------------+-----------------+---------------------
  0 | Anna | Bianchi | 2012-04-18 | Pegasus       | Didattica            |               8 |                   4
(1 row)

############################################################

-- 10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono assenti e hanno attività progettuali?

select distinct p.nome, p.cognome
from persona p
JOIN assenza a on a.persona = p.id
JOIN attivitaprogetto at on at.persona = p.id
where at.giorno = a.giorno;

-- alternativa:
select distinct p.nome, p.cognome
from persona p, assenza a, attivitaprogetto atp
where p.id = a.persona
	and p.id = atp.persona
	and a.giorno = atp.giorno;

 id | nome | cognome 
----+------+---------
  0 | Anna | Bianchi
(1 row)

############################################################

-- 11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il nome del progetto, la causa di assenza e la durata in ore della attività progettuale.

select distinct p.nome, p.cognome, a.giorno, prog.nome as progetto, a.tipo as tipo_assenza, atp.oredurata
from persona p, assenza a, progetto prog, attivitaprogetto atp
where p.id = a.persona
	and p.id = atp.persona
	and a.giorno = atp.giorno
	and prog.id = atp.progetto;

  -- alternativa:
select distinct p.nome, p.cognome, a.giorno, prog.nome as progetto, a.tipo as tipo_assenza, atp.oredurata
from persona p
join assenza a on p.id = a.persona
join attivitaprogetto atp on p.id = atp.persona
join progetto prog on prog.id = atp.progetto
where a.giorno = atp.giorno;

 id | nome | cognome |   giorno   | nome_progetto | causa_assenza | ore_progettuali 
----+------+---------+------------+---------------+---------------+-----------------
  0 | Anna | Bianchi | 2012-04-18 | Pegasus       | Malattia      |               8
(1 row)

############################################################

--12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?

select distinct wp1.nome
from wp as wp1, wp as wp2
where wp1.progetto <> wp2.progetto
	and wp1.nome = wp2.nome;

--alternativa:
select distinct wp1.nome
from wp as wp1
join wp as wp2 on wp1.nome = wp2.nome
where wp1.progetto <> wp2.progetto;

 nome 
------
 WP1
 WP2
 WP3
(3 rows)

############################################################
