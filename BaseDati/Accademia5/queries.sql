Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

1. Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome
‘Pegasus’ ?

SELECT wp.id, wp.nome, wp.inizio, wp.fine
FROM WP wp
JOIN Progetto p ON wp.progetto = p.id
WHERE p.nome = 'Pegasus';

 id | nome |   inizio   |    fine    
----+------+------------+------------
  0 | WP1  | 2012-01-01 | 2012-12-31
  1 | WP2  | 2012-01-01 | 2012-12-31
  2 | WP3  | 2013-01-01 | 2013-12-31
(3 rows)

############################################################

2. Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno
una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?

SELECT DISTINCT pers.id, pers.nome, pers.cognome, pers.posizione
FROM Persona pers
JOIN AttivitaProgetto att ON pers.id = att.persona
JOIN Progetto p ON att.progetto = p.id
WHERE p.nome = 'Pegasus'
ORDER BY pers.cognome DESC;

 id |  nome   | cognome  |      posizione       
----+---------+----------+----------------------
 10 | Ginevra | Riva     | Professore Ordinario
  8 | Asia    | Giordano | Professore Ordinario
  2 | Barbara | Burso    | Ricercatore
  0 | Anna    | Bianchi  | Ricercatore
(4 rows)

############################################################

3. Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di
una attività nel progetto ‘Pegasus’ ?

SELECT pers.id, pers.nome, pers.cognome, pers.posizione
FROM Persona pers
JOIN AttivitaProgetto att ON pers.id = att.persona
JOIN Progetto p ON att.progetto = p.id
WHERE p.nome = 'Pegasus'
GROUP BY pers.id, pers.nome, pers.cognome, pers.posizione
HAVING COUNT(att.id) > 1;

 id | nome | cognome |  posizione  
----+------+---------+-------------
  0 | Anna | Bianchi | Ricercatore
(1 row)

############################################################

4. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
fatto almeno una assenza per malattia?

SELECT DISTINCT pers.id, pers.nome, pers.cognome, pers.posizione
FROM Persona pers
JOIN Assenza ass ON pers.id = ass.persona
WHERE pers.posizione = 'Professore Ordinario' AND ass.tipo = 'Malattia';

 id |  nome   | cognome  |      posizione       
----+---------+----------+----------------------
  8 | Asia    | Giordano | Professore Ordinario
 10 | Ginevra | Riva     | Professore Ordinario
(2 rows)

############################################################

5. Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno
fatto più di una assenza per malattia?

SELECT pers.id, pers.nome, pers.cognome, pers.posizione
FROM Persona pers
JOIN Assenza ass ON pers.id = ass.persona
WHERE pers.posizione = 'Professore Ordinario' AND ass.tipo = 'Malattia'
GROUP BY pers.id, pers.nome, pers.cognome, pers.posizione
HAVING COUNT(ass.id) > 1;

 id |  nome   | cognome |      posizione       
----+---------+---------+----------------------
 10 | Ginevra | Riva    | Professore Ordinario
(1 row)

############################################################

6. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno
un impegno per didattica?

SELECT DISTINCT pers.id, pers.nome, pers.cognome, pers.posizione
FROM Persona pers
JOIN AttivitaNonProgettuale attnp ON pers.id = attnp.persona
WHERE pers.posizione = 'Ricercatore' AND attnp.tipo = 'Didattica';

 id |  nome   | cognome |  posizione  
----+---------+---------+-------------
  0 | Anna    | Bianchi | Ricercatore
  1 | Mario   | Rossi   | Ricercatore
  2 | Barbara | Burso   | Ricercatore
(3 rows)

############################################################

7. Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno più di un
impegno per didattica?

SELECT pers.id, pers.nome, pers.cognome, pers.posizione
FROM Persona pers
JOIN AttivitaNonProgettuale attnp ON pers.id = attnp.persona
WHERE pers.posizione = 'Ricercatore' AND attnp.tipo = 'Didattica'
GROUP BY pers.id, pers.nome, pers.cognome, pers.posizione
HAVING COUNT(attnp.id) > 1;

 id |  nome   | cognome |  posizione  
----+---------+---------+-------------
  2 | Barbara | Burso   | Ricercatore
(1 row)

############################################################

8. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
attività progettuali che attività non progettuali?

SELECT DISTINCT pers.id, pers.nome, pers.cognome
FROM Persona pers
JOIN AttivitaProgetto attp ON pers.id = attp.persona
JOIN AttivitaNonProgettuale attnp ON pers.id = attnp.persona AND attp.giorno = attnp.giorno;

 id | nome | cognome 
----+------+---------
  0 | Anna | Bianchi
(1 row)

############################################################

9. Quali sono il nome e il cognome degli strutturati che nello stesso giorno hanno sia
attività progettuali che attività non progettuali? Si richiede anche di proiettare il
giorno, il nome del progetto, il tipo di attività non progettuali e la durata in ore di
entrambe le attività.

SELECT DISTINCT pers.id, pers.nome, pers.cognome, attp.giorno, proj.nome AS nome_progetto, attnp.tipo AS tipo_non_progettuale, attp.oreDurata AS ore_progettuali, attnp.oreDurata AS ore_non_progettuali
FROM Persona pers
JOIN AttivitaProgetto attp ON pers.id = attp.persona
JOIN Progetto proj ON attp.progetto = proj.id
JOIN AttivitaNonProgettuale attnp ON pers.id = attnp.persona AND attp.giorno = attnp.giorno;

 id | nome | cognome |   giorno   | nome_progetto | tipo_non_progettuale | ore_progettuali | ore_non_progettuali 
----+------+---------+------------+---------------+----------------------+-----------------+---------------------
  0 | Anna | Bianchi | 2012-04-18 | Pegasus       | Didattica            |               8 |                   4
(1 row)

############################################################

10. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
assenti e hanno attività progettuali?

SELECT DISTINCT pers.id, pers.nome, pers.cognome
FROM Persona pers
JOIN AttivitaProgetto attp ON pers.id = attp.persona
JOIN Assenza ass ON pers.id = ass.persona AND attp.giorno = ass.giorno;

 id | nome | cognome 
----+------+---------
  0 | Anna | Bianchi
(1 row)

############################################################

11. Quali sono il nome e il cognome degli strutturati che nello stesso giorno sono
assenti e hanno attività progettuali? Si richiede anche di proiettare il giorno, il
nome del progetto, la causa di assenza e la durata in ore della attività progettuale.

SELECT DISTINCT pers.id, pers.nome, pers.cognome, ass.giorno, proj.nome AS nome_progetto, ass.tipo AS causa_assenza, attp.oreDurata AS ore_progettuali
FROM Persona pers
JOIN AttivitaProgetto attp ON pers.id = attp.persona
JOIN Progetto proj ON attp.progetto = proj.id
JOIN Assenza ass ON pers.id = ass.persona AND attp.giorno = ass.giorno;

 id | nome | cognome |   giorno   | nome_progetto | causa_assenza | ore_progettuali 
----+------+---------+------------+---------------+---------------+-----------------
  0 | Anna | Bianchi | 2012-04-18 | Pegasus       | Malattia      |               8
(1 row)

############################################################

12. Quali sono i WP che hanno lo stesso nome, ma appartengono a progetti diversi?

SELECT DISTINCT wp1.nome                                                      
FROM WP wp1
JOIN WP wp2 ON wp1.nome = wp2.nome AND wp1.progetto <> wp2.progetto;

 nome 
------
 WP1
 WP2
 WP3
(3 rows)

############################################################
