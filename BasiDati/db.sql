begin transaction;

-- Creazione dei domini

create domain PosInteger as integer check (value > 0);

create domain StringaM as varchar(100);

create domain Email as varchar(100) check (value ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');

create domain Reale0_1 as real check (value >= 0 and value <= 1);

-- Creazione dello schema relazionale

create table Cliente (
  nome StringaM not null,
  cognome StringaM not null,
  email Email not null,
  primary key (email)  
);

create table Ristorante (
  nome StringaM not null,
  partitaIVA StringaM not null,
  id serial not null,
  primary key (id)  
);

create table Promozione (
  nome StringaM not null,
  sconto Reale0_1 not null,
  n_coperti PosInteger not null,
  primary key (nome)  
);

create table Prenotazione (
  cliente Email not null,
  ristorante integer not null,
  Promozione StringaM,
  istante_pren timestamp not null,
  istante_app timestamp not null,
  n_coperti integer check (n_coperti > 0),
  prenot_utlizzata timestamp,
  id serial not null,
  primary key (id),
  foreign key (cliente) references Cliente(email),
  foreign key (ristorante) references Ristorante(id),
  foreign key (Promozione) references Promozione(nome),
  unique (ristorante, cliente, istante_pren),
  check (istante_app > istante_pren),
  check (prenot_utlizzata is null or (prenot_utlizzata > istante_pren and prenot_utlizzata > istante_app))
);


commit;
