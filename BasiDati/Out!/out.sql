CREATE TABLE Nazione(
    nome varchar not null,
    primary key(nome)
);

CREATE TABLE Regione(
    nome varchar not null,
    nazione varchar not null,
    primary key (nome, nazione),
    foreign key nazione references Nazione(nome)
);

CREATE TABLE Citta(
    nome varchar not null,
    regione varchar not null,
    nazione varchar not null,
    primary key (nome, regione, nazione),
    foreign key (regione, nazione) 
        references Regione(nome, nazione)
);

CREATE TABLE Sede(
    id serial primary key not null,
    indirizzo Indirizzo not null,
    nome varchar not null,
    citta varchar not null,
    regione varchar not null,
    nazione varchar not null,
    foreign key (citta, regione, nazione) 
        references Cita(nome, regione, nazione)
); -- v.incl id occore in Sala

CREATE TABLE Sala(
    nome varchar not null,
    sede integer not null,
    primary key (nome, sede)
    foreign key sede
        references Sede(id)
);

CREATE TABLE Settore(
    id serial primary key not null,
    nome varchar not null,
    sala varchar not null,
    sede integer not null,
    unique (nome, sala, sede),
    foreign key(sala, sede)
        references Sala(nome, sede)
);

CREATE TABLE Posto(
    fila integer not null,
    colomna integer not null,
    settore integer not null,
    primary key (fila, colomna, settore),
    foreign key settore
        references Settore(id)
);

CREATE TABLE Artista(
    id serial primary key not null,
    nome varchar not null,
    cognome varchar not null,
    nome_arte varchar
); -- v.incl id occore in Spettacolo

CREATE TABLE TipologiaSpettacolo(
    nome varchar primary key not null,
);

CREATE TABLE Genere(
    nome varchar primary key not null,
);

CREATE TABLE Spettacolo(
    id serial primary key not null,
    nome varchar not null,
    durata_min integer not null,
    tipologia varchar not null,
    genere varchar not null,
    foreign key tipologia
        references TipologiaSpettacolo(nome),
    foreign key genere
        references Genere(nome)
); 

CREATE TABLE partecipa(
    spettacolo integer not null,
    artista integer not null,
    primary key(spettacolo, artista)
    foreign key spettacolo
        references Spettacolo(id),
    foreign key artista
        references Artista(id)
); 

CREATE TABLE Evento(
    id serial primary key not null,
    data date not null,
    orario time not null,
    spettacolo integer not null,
    sede varchar not null, 
    sala varchar not null,
    foreign key spettacolo
        references Spettacolo(id),
    foreign key (sede, sala)
        references Sala(sede, nome)
);

CREATE TABLE Utente(
    nome varchar not null,
    cognome varchar not null,
    cf Cf primary key not null,
);

CREATE TABLE Prenotazione(
    id serial primary key not null,
    istante timestamp not null,
    evento integer not null,
    utente Cf not null,
    foreign key evento
        references Evento(id),
    foreign key utente
        references Utente(cf)
); -- v.incl id occore in pre_posto(prenotazione)

CREATE TABLE TipoTariffa(
    nome varchar primary key not null,
);

CREATE TABLE Tariffa(
    prezzo Denaro not null,
    tipotariffa varchar primary key not null,
    settore integer not null,
    foreign key tipotariffa
        references TipoTariffa(nome)
    foreign key settore
        references Settore(id)
);

CREATE TABLE pre_posto(
    prenotazione integer not null,
    fila integer not null,
    colomna integer not null,
    settore integer not null,
    tipotariffa varchar not null,
    primary key (prenotazione, fila, colomna, settore)
    foreign key prenotazione
        references Prenotazione(id),
    foreign key (fila, colomna, settore)
        references Posto(fila, colomna, settore),
    foreign key tipotariffa
        references TipoTariffa(nome)
); 