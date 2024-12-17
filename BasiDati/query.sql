-- QUERY 1

SELECT p.nome, p.cognome, COUNT(DISTINCT ap.progetto) AS numero_progetti
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
WHERE p.posizione = 'Professore Ordinario'
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 2

SELECT p.nome, p.cognome, AVG(ap.oreDurata) AS media_ore
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
WHERE p.posizione = 'Ricercatore'
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 3

SELECT nome, cognome, stipendio
FROM Persona
WHERE stipendio >= 60000;

-- QUERY 4 

SELECT p.nome, p.cognome, SUM(pr.budget) AS budget_totale
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
JOIN Progetto pr ON ap.progetto = pr.id
WHERE p.posizione = 'Professore Associato'
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 5

SELECT p.nome, p.cognome, COUNT(a.giorno) AS giorni_assenza_maternita
FROM Persona p
JOIN Assenza a ON p.id = a.persona
WHERE p.posizione = 'Ricercatore' AND a.tipo = 'Maternita'
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 6

SELECT AVG(budget) AS budget_medio
FROM Progetto;

-- QUERY 7

SELECT p.nome, p.cognome, SUM(ap.oreDurata) AS ore_totali
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
WHERE ap.progetto = 3
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 8

SELECT p.nome, p.cognome, SUM(ap.oreDurata) AS ore_totali
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
WHERE p.posizione = 'Professore Ordinario' 
  AND ap.wp = 3 
  AND ap.progetto = 4
GROUP BY p.id, p.nome, p.cognome;

-- QUERY 9

SELECT DISTINCT p.nome, p.cognome, p.stipendio
FROM Persona p
JOIN AttivitaProgetto ap ON p.id = ap.persona
WHERE p.posizione = 'Professore Ordinario' AND p.stipendio >= 60000;

-- QUERY 10

SELECT p.nome, p.cognome, AVG(anp.oreDurata) AS media_ore_didattiche
FROM Persona p
JOIN AttivitaNonProgettuale anp ON p.id = anp.persona
WHERE anp.tipo = 'Didattica'
GROUP BY p.id, p.nome, p.cognome;