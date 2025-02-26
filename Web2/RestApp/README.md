# Dashboard Accademia

Questa applicazione è stata sviluppata come progetto d'esame per il corso Web 2 - Cybersecurity Specialist 2023/2025. Il sistema combina un backend Flask con un frontend React per visualizzare ed interagire con i dati del database SQLite Accademia.



## Funzionalità Principali

- **Visualizzazione Dati**: Interfaccia intuitiva per esplorare e analizzare i dati relativi a persone, progetti, work packages, attività e assenze.
- **Filtri Avanzati**: Possibilità di filtrare i dati per vari campi.
- **Statistiche e Dashboard**: Ogni sezione include grafici e statistiche di riepilogo per una rapida analisi dei dati.
- **API RESTful**: Backend Flask che espone i dati tramite API REST.



## Struttura del Progetto

Il progetto è suddiviso in due parti principali: Backend (Flask) e Frontend (React).

### Backend (Flask)

- **sqlliterestapi.py**: Il server API che gestisce le richieste e comunica con il database.
- **database.db**: Database SQLite contenente le tabelle per persone, progetti, WPs, attività e assenze.

### Frontend (React)

- **App.jsx**: Componente principale che gestisce il routing dell'applicazione.
- **Home.jsx**: Dashboard principale con statistiche generali e accesso alle varie sezioni.
- **Navbar.jsx**: Barra di navigazione per accedere alle diverse parti dell'applicazione.
- **Componenti specifici**: Persona.jsx, Progetti.jsx, WPs.jsx, AttivitaProgetto.jsx, AttivitaNonProgettuale.jsx, Assenza.jsx, HomeAlert.jsx.
- **Stili**: CSS personalizzati per migliorare l'aspetto dell'interfaccia utente.



## Guida all'Installazione

### Requisiti

- Python 3.7 o superiore
- Node.js 14 o superiore
- npm

### Installazione Backend

1. Clona il repository:
   ```
   git clone https://github.com/jvfdalmas/EsameWeb2CyberSec2325.git
   cd EsameWeb2CyberSec2325/RestApp
   ```

2. Crea un ambiente virtuale e attivalo:
   ```
   python3 -m venv venv
   source venv/bin/activate  # Su Windows: venv\Scripts\activate
   ```

3. Installa le dipendenze:
   ```
   pip install -r requirements.txt
   ```

4. Avvia il server Flask:
   ```
   python3 sqlliterestapi.py
   ```
   Il server sarà in esecuzione su http://localhost:8080

### Installazione Frontend

1. Installa le dipendenze:
   ```
   npm install
   ```

2. Avvia l'applicazione React:
   ```
   npm run dev
   ```
   L'applicazione dovrà essere avviata nel browser (in genere su http://localhost:3000, ma deve essere controllato nella bash)



## Guida all'Utilizzo

### 1. Dashboard Home

La home page offre una panoramica generale con:
- Statistiche sul numero totale di persone, progetti, WPs, attività e assenze.
- Pulsanti per accedere rapidamente alle diverse sezioni dell'applicazione.
- Un messaggio di benvenuto che spiega lo scopo dell'applicazione.

### 2. Visualizzazione Tabelle

Ogni sezione dell'applicazione (Persone, Progetti, WPs, Attività, Assenze) presenta:
- Una tabella con tutti i dati relativi alla specifica entità.
- Filtri per cercare informazioni specifiche (es. filtrare per nome persona, nome progetto).
- Conteggio totale degli elementi visualizzati.

### 3. Utilizzo dei Filtri

1. Seleziona il campo su cui filtrare dal menu a discesa (es. "Persona", "Progetto", "Data").
2. Inserisci il valore da cercare nella casella di testo.
3. La tabella si aggiornerà automaticamente mostrando solo le righe che corrispondono al filtro.

### 4. Visualizzazione Statistiche

Ogni sezione include una o più dashboard con:
- Statistiche di riepilogo (es. ore totali, stipendio medio).
- Distribuzione dei dati per categoria (es. assenze per persona, ore per tipo di attività).
- Grafici e tabelle per facilitare l'analisi dei dati.

## Struttura Database

L'applicazione utilizza un database SQLite con le seguenti tabelle:

- **Persona**: Informazioni sul personale (id, nome, cognome, posizione, stipendio).
- **Progetto**: Dettagli sui progetti (id, nome, inizio, fine, budget).
- **WP**: Work Packages legati ai progetti (id, progetto, nome, inizio, fine).
- **AttivitaProgetto**: Attività legate a progetti specifici (id, persona, progetto, wp, giorno, tipo, oreDurata).
- **AttivitaNonProgettuale**: Attività non legate a progetti (id, persona, tipo, giorno, oreDurata).
- **Assenza**: Assenze del personale (id, persona, tipo, giorno).




## Crediti

Sviluppato come progetto d'esame per il corso Web 2 - Cybersecurity Specialist 2023/2025.

---