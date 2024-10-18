create domain PosInteger as integer check (value >= 0);

create domain Indirizzo as varchar(100);

create domain CodFis as integer check (value >= 0);

CREATE TABLE Nazione
(nome varchar not null,
PRIMARY KEY nome
);

CREATE TABLE Regione
(nome varchar not null, 
nazione varchar not null,
PRIMARY KEY (nome, nazione),
FOREIGN KEY nazione 
    REFERENCES Nazione(nome)
    );

CREATE TABLE Citta
(nome varchar not null,
regione varchar not null,
nazione varchar not null,
PRIMARY KEY (nome, regione, nazione),
FOREIGN KEY (regione, nazione) 
    REFERENCES Regione(nome, nazione)
);

CREATE TABLE TipoVeicolo
(nome varchar not null,
PRIMARY KEY(nome)
);

CREATE TABLE Marca
(nome varchar not null,
PRIMARY KEY(nome)
);

CREATE TABLE Modello
(nome varchar not null,
marca varchar not null,
tipo varchar not null,
PRIMARY KEY (nome, marca),
FOREIGN KEY marca 
    REFERENCES Marca(nome),
FOREIGN KEY tipo
    REFERENCES TipoVeicolo(nome)
);

CREATE TABLE Veicolo
(targa varchar not null,
immatricolazione PosInteger not null,
modello varchar not null,
marca varchar not null,
proprietario varchar not null,
PRIMARY KEY(targa),
FOREIGN KEY (modello, marca) 
    REFERENCES Modello(nome, marca)
FOREIGN KEY proprietario 
    REFERENCES Cliente(cf)
);

CREATE TABLE Riparazione
(codice varchar not null,
riconsenga varchar,
inizio timestamp not null,
PRIMARY KEY(codice)
);

CREATE TABLE Officina
(id PosInteger not null,
nome varchar not null,
indirizzo varchar not null,
citta varchar not null,
regione varchar not null,
nazione varchar not null,
PRIMARY KEY(id),
FOREIGN KEY (citta, regione, nazione) 
    REFERENCES Citta(nome, regione, nazione)
);

CREATE TABLE off_rip
(officina PosInteger not null,
riparazione varchar not null,
PRIMARY KEY(riparazione),
FOREIGN KEY officina 
    REFERENCES Officina(id) deferrable,
FOREIGN KEY riparazione 
    REFERENCES Riparazione(codice) deferrable
);

ALTER TABLE Riparazione
    ADD FOREIGN KEY (codice) references off_rip(riparazione) deferrable;

CREATE TABLE Persona
(cf CodFis not null,
nome varchar not null,
indirizzo Indirizzo not null,
telefono PosInteger not null,
citta varchar not null,
regione varchar not null,
nazione varchar not null,
PRIMARY KEY(cf),
FOREIGN KEY (citta, regione, nazione) 
    REFERENCES Citta(nome, regione, nazione)
);

CREATE TABLE Cliente
(persona CodFis not null,
PRIMARY KEY(persona)
FOREIGN KEY persona 
    REFERENCES Persona(cf)
);

CREATE TABLE Staff
(persona CodFis not null,
PRIMARY KEY(persona)
FOREIGN KEY persona 
    REFERENCES Persona(cf)
);

CREATE TABLE Dipendente
(persona CodFis not null,
PRIMARY KEY(persona)
FOREIGN KEY persona 
    REFERENCES Staff(persona)
);

CREATE TABLE Lavora
(assunzione data not null,
lavoratore CodFis not nul,
officina PosInteger not null,
FOREIGN KEY lavoratore 
    REFERENCES Staff(persona),
FOREIGN KEY officina 
    REFERENCES Officina(id)
);

CREATE TABLE Direttore
(nascita date not null,
persona CodFis not null,
PRIMARY KEY(persona)
FOREIGN KEY persona 
    REFERENCES Persona(cf)
);