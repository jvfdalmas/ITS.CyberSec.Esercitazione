begin transaction;

-- Creazione dei domini

-- PosInteger: numeri interi positivi (>0)
CREATE DOMAIN PosInteger AS INTEGER 
CHECK (VALUE > 0);

-- PosIntegerZero: numeri interi non negativi (>=0)
CREATE DOMAIN PosIntegerZero AS INTEGER 
CHECK (VALUE >= 0);

-- Stringa non nulla e di massimo 100 caratteri
CREATE DOMAIN StrMNotNull AS VARCHAR(100)
CHECK (VALUE IS NOT NULL AND LENGTH(VALUE) > 0);

-- Creazione di un dominio per il Codice Fiscale
CREATE DOMAIN CodiceFiscale AS CHAR(16)
CHECK (
    VALUE ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$'
);

-- Partita IVA
CREATE DOMAIN PartitaIVA AS CHAR(11)
CHECK (VALUE ~ '^[0-9]{11}$');

-- CAP - Codice di Avviamento Postale italiano
CREATE DOMAIN CAPNotNull AS CHAR(5) 
CHECK (VALUE ~ '^[0-9]{5}$');

-- Codice postale generico non limitati all'Italia:
CREATE DOMAIN CAPGenerico AS VARCHAR(10)
CHECK (VALUE ~ '^[A-Za-z0-9- ]+$');

-- Tipo di indirizzo strutturato
CREATE TYPE Indirizzo AS (
    via StrMNotNull, 
    civico StrMNotNull, 
    cap CAPNotNull
);

-- Tipo enumerativo
-- Stato Civile
CREATE TYPE StatoCivile AS ENUM ('Celibe', 'Nubile', 'Sposato', 'Sposata', 'Divorziato', 'Divorziata', 'Vedovo', 'Vedova');
-- Ruolo Utente
CREATE TYPE RuoloUtente AS ENUM ('Amministratore', 'Moderatore', 'Utente', 'Ospite');

-- Stati Binari (Boolean)
CREATE DOMAIN StatoAttivo AS BOOLEAN;

-- Denaro: creazione di un tipo strutturato per il denaro con valuta
CREATE TYPE Denaro AS (
    importo REAL,
    valuta CHAR(3));


-- Eta
CREATE DOMAIN Eta AS INTEGER 
CHECK (VALUE >= 0 AND VALUE <= 120);

-- Valutazione
CREATE DOMAIN Valutazione AS NUMERIC(3, 1) 
CHECK (VALUE >= 0 AND VALUE <= 5);

-- Email
CREATE DOMAIN Email AS VARCHAR(254)
CHECK (VALUE ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');

-- Telefono
CREATE DOMAIN Telefono AS VARCHAR(15)
CHECK (VALUE ~ '^\+[1-9][0-9]{1,14}$');

-- Percentuale
CREATE DOMAIN Percentuale AS NUMERIC(5, 2) 
CHECK (VALUE >= 0 AND VALUE <= 100);

-- IBAN
CREATE DOMAIN IBAN AS VARCHAR(34)
CHECK (VALUE ~ '^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$');








-- Creazione dello schema relazionale

create table Compagnia(
  nome StringaM not null,
  annoFondaz PosInteger null,
  primary key (nome)
);

create table Aeroporto (
  codice CodIATA not null,
  nome StringaM not null,
  primary key (codice)  
);

create table LuogoAeroporto (
    aeroporto CodIATA not null,
    citta StringaM not null,
    nazione StringaM not null,
    primary key (aeroporto),
    foreign key (aeroporto) references Aeroporto(codice) deferrable -- 
);--  l'opzione DEFERRABLE è inclusa nelle dichiarazioni delle chiavi esterne (foreign key) per indicare che i vincoli di integrità referenziale possono essere rinviati, cioè non vengono verificati immediatamente quando viene eseguita un'operazione (come un INSERT o un UPDATE), ma piuttosto alla fine della transazione corrente.

alter table ArrPart
add foreign key (codice, comp) references Volo(codice, comp) deferrable;


commit;