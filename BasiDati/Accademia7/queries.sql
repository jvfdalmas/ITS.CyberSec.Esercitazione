-- Definire in SQL le seguenti interrogazioni, in cui si chiedono tutti risultati distinti:

############################################################

-- 1. Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?

SELECT 
    posizione, 
    AVG(stipendio) AS media_stipendio, 
    STDDEV(stipendio) AS dev_standard
FROM 
    Persona
GROUP BY 
    posizione;

############################################################

--2. Quali sono i ricercatori (tutti gli attributi) con uno stipendio superiore alla media della loro categoria?

WITH MediaRicercatori AS (
    SELECT 
        posizione, 
        AVG(stipendio) AS media_stipendio
    FROM 
        Persona
    WHERE 
        posizione = 'Ricercatore'
    GROUP BY 
        posizione
)
SELECT p.*
FROM Persona p
JOIN MediaRicercatori m ON p.posizione = 'Ricercatore'
WHERE p.stipendio > m.media_stipendio;

############################################################

--3. Per ogni categoria di strutturati quante sono le persone con uno stipendio che differisce di al massimo una deviazione standard dalla media della loro categoria?

SELECT 
    p1.posizione, 
    COUNT(*) AS persone_entro_dev_standard
FROM 
    Persona p1
JOIN (
    SELECT 
        posizione, 
        AVG(stipendio) AS media_stipendio, 
        STDDEV(stipendio) AS dev_standard
    FROM 
        Persona
    GROUP BY 
        posizione
) stats ON p1.posizione = stats.posizione
WHERE 
    ABS(p1.stipendio - stats.media_stipendio) <= stats.dev_standard
GROUP BY 
    p1.posizione;

############################################################

--4. Chi sono gli strutturati che hanno lavorato almeno 20 ore complessive in attività progettuali? Restituire tutti i loro dati e il numero di ore lavorate.

WITH OreTotali AS (
    SELECT 
        a.persona, 
        SUM(a.oreDurata) AS ore_totali
    FROM 
        AttivitaProgetto a
    GROUP BY 
        a.persona
)
SELECT 
    p.*, 
    o.ore_totali
FROM 
    Persona p
JOIN 
    OreTotali o ON p.id = o.persona
WHERE 
    o.ore_totali >= 20;

############################################################

--5. Quali sono i progetti la cui durata è superiore alla media delle durate di tutti i progetti? Restituire nome dei progetti e loro durata in giorni.

WITH MediaDurataProgetti AS (
    SELECT 
        AVG(fine - inizio) AS media_durata
    FROM 
        Progetto
)
SELECT 
    p.nome, 
    (p.fine - p.inizio) AS durata_giorni
FROM 
    Progetto p, MediaDurataProgetti m
WHERE 
    (p.fine - p.inizio) > m.media_durata;



############################################################

--6. Quali sono i progetti terminati in data odierna che hanno avuto attività di tipo “Dimostrazione”? Restituire nome di ogni progetto e il numero complessivo delle ore dedicate a tali attività nel progetto.

WITH ProgettiTerminati AS (
    SELECT 
        id AS progetto_id, 
        nome AS nome_progetto
    FROM 
        Progetto
    WHERE 
        fine = CURRENT_DATE
),
AttivitaDimostrazione AS (
    SELECT 
        progetto, 
        SUM(oreDurata) AS ore_totali_dimostrazione
    FROM 
        AttivitaProgetto
    WHERE 
        tipo = 'Dimostrazione'
    GROUP BY 
        progetto
)
SELECT 
    pt.nome_progetto, 
    ad.ore_totali_dimostrazione
FROM 
    ProgettiTerminati pt
JOIN 
    AttivitaDimostrazione ad 
    ON pt.progetto_id = ad.progetto;


############################################################

--7. Quali sono i professori ordinari che hanno fatto più assenze per malattia del nu- mero di assenze medio per malattia dei professori associati? Restituire id, nome e cognome del professore e il numero di giorni di assenza per malattia

WITH MediaAssenzeAssociati AS (
    SELECT 
        AVG(assenze.giorni_assenza) AS media_assenze
    FROM (
        SELECT 
            p2.id, 
            COUNT(a2.id) AS giorni_assenza
        FROM 
            Persona p2
        JOIN 
            Assenza a2 ON p2.id = a2.persona
        WHERE 
            p2.posizione = 'Professore Associato' 
            AND a2.tipo = 'Malattia'
        GROUP BY 
            p2.id
    ) assenze
)
SELECT 
    p.id, 
    p.nome, 
    p.cognome, 
    COUNT(a.id) AS giorni_totali_malattia
FROM 
    Persona p
JOIN 
    Assenza a ON p.id = a.persona
JOIN 
    MediaAssenzeAssociati m ON TRUE
WHERE 
    p.posizione = 'Professore Ordinario' 
    AND a.tipo = 'Malattia'
GROUP BY 
    p.id, p.nome, p.cognome, m.media_assenze
HAVING 
    COUNT(a.id) > m.media_assenze;

############################################################