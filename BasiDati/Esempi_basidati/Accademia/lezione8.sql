create database accademia;
\c accademia;
 
create domain PosInteger as integer check (value >= 0);
create domain StringaM as varchar(100);
create domain NumeroOre as integer check (8>= value and value >= 0);
create domain Denaro as real check (value >= 0);

create type Strutturato as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario');
create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro');
create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro
Accademico', 'Altro');
create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia');

create table Persona (id PosInteger primary key, nome StringaM  not null, cognome StringaM  not null, posizione Strutturato not null, stipendio Denaro default 0, unique (nome, cognome));
create  table Progetto (id PosInteger primary key, nome StringaM  not null, inizio date not null, fine date not null, budget Denaro default 0, check (inizio < fine), unique (nome));
create table WP (progetto PosInteger not null, id PosInteger not null, nome StringaM not null, inizio date not null, fine date not null, primary key (progetto, id), check (inizio < fine), foreign key (progetto) references Progetto(id), unique (progetto, nome));
create table AttivitaProgetto (id PosInteger primary key, persona PosInteger not null, progetto PosInteger not null,
wp PosInteger not null, giorno date not null, tipo LavoroProgetto not null, oreDurata timestamp not null, foreign key (persona) references Persona(id), foreign key (progetto, wp) references WP(progetto, id));
create table AttivitaNonProgettuale (id PosInteger primary key, persona PosInteger not null, tipo LavoroNonProgettuale not null, giorno date not null, oreDurata timestamp not null, foreign key (persona) references Persona(id));
create table Assenza (id PosInteger primary key, persona PosInteger not null, tipo CausaAssenza not null, giorno date not null, foreign key (persona) references Persona(id), unique (persona, giorno));
