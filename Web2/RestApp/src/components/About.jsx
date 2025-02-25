import React from 'react';
import { Container, Card, ListGroup, Alert } from 'react-bootstrap';

const About = () => {
  return (
    <Container className="my-5">
      <h1 className="text-center mb-5">About - Dashboard Accademia</h1>
      
      <Alert variant="info" className="mb-4">
        <Alert.Heading>Progetto d'esame</Alert.Heading>
        <p>
          Questa applicazione è stata sviluppata come parte dell'esame del corso Web 2 - Cybsercurity Specialist 2023/2025. 
          Il sistema integra un backend Flask con un frontend React per la gestione di
          progetti, persone, attività e assenze in ambito aziendale.
        </p>
      </Alert>

      <Card className="mb-5">
        <Card.Header as="h2">Funzionalità del Sistema</Card.Header>
        <Card.Body>
          <p>
            Questo sistema di gestione consente di visualizzare e filtrare dati relativi a progetti, 
            persone, work packages, attività e assenze. Ogni sezione dell'applicazione è 
            rappresentata da una pagina dedicata con funzionalità di filtro avanzate.
          </p>
        </Card.Body>
      </Card>

      <h2 className="mb-4">Pagine dell'Applicazione</h2>

      <Card className="mb-4">
        <Card.Header as="h3">Persone</Card.Header>
        <Card.Body>
          <p>
            La pagina <strong>Persone</strong> visualizza l'elenco completo del personale con 
            informazioni su ID, nome, cognome, posizione lavorativa e stipendio. È possibile 
            filtrare i dati per qualsiasi campo per trovare rapidamente specifici membri del team.
          </p>
        </Card.Body>
      </Card>

      <Card className="mb-4">
        <Card.Header as="h3">Progetti</Card.Header>
        <Card.Body>
          <p>
            La pagina <strong>Progetti</strong> elenca tutti i progetti dell'organizzazione, 
            mostrando i dettagli come ID, nome, date di inizio e fine, e budget allocato. 
            Il sistema di filtro permette di identificare rapidamente progetti specifici in base
            a qualsiasi parametro.
          </p>
        </Card.Body>
      </Card>

      <Card className="mb-4">
        <Card.Header as="h3">Work Packages (WPs)</Card.Header>
        <Card.Body>
          <p>
            La sezione <strong>Work Packages</strong> mostra i pacchetti di lavoro associati a 
            ciascun progetto. Oltre all'ID e al nome del WP, vengono visualizzate le date di 
            inizio e fine, e il nome del progetto a cui appartiene ogni WP. La funzionalità di
            filtro facilita la ricerca tra numerosi work packages.
          </p>
        </Card.Body>
      </Card>

      <Card className="mb-4">
        <Card.Header as="h3">Attività di Progetto</Card.Header>
        <Card.Body>
          <p>
            La pagina <strong>Attività di Progetto</strong> presenta un registro dettagliato di tutte 
            le attività svolte nell'ambito dei progetti. Ogni record include informazioni sulla persona 
            coinvolta, il progetto e il work package di riferimento, la data, il tipo di attività e 
            le ore dedicate. Il sistema visualizza i nomi effettivi anziché semplici ID, per una migliore
            leggibilità.
          </p>
        </Card.Body>
      </Card>

      <Card className="mb-4">
        <Card.Header as="h3">Attività Non Progettuali</Card.Header>
        <Card.Body>
          <p>
            La sezione <strong>Attività Non Progettuali</strong> traccia le attività che non sono 
            legate a specifici progetti, come riunioni dipartimentali, didattica o missioni. 
            Ogni record mostra la persona coinvolta, il tipo di attività, la data e le ore dedicate.
            La pagina include anche un riepilogo delle ore totali per ogni tipo di attività.
          </p>
        </Card.Body>
      </Card>

      <Card className="mb-4">
        <Card.Header as="h3">Assenze</Card.Header>
        <Card.Body>
          <p>
            La pagina <strong>Assenze</strong> registra tutte le assenze del personale, specificando 
            la persona, il tipo di assenza e la data. Include inoltre una dashboard con statistiche 
            che evidenziano la distribuzione delle assenze per tipologia e per persona, offrendo 
            una panoramica immediata dei pattern di assenza.
          </p>
        </Card.Body>
      </Card>

      <Card className="mb-5">
        <Card.Header as="h2">Tecnologie Utilizzate</Card.Header>
        <Card.Body>
          <ListGroup variant="flush">
            <ListGroup.Item>
              <strong>Backend:</strong> Flask (Python) con SQLAlchemy per l'ORM e SQLite come database
            </ListGroup.Item>
            <ListGroup.Item>
              <strong>Frontend:</strong> React.js con componenti React Bootstrap per l'interfaccia utente
            </ListGroup.Item>
            <ListGroup.Item>
              <strong>API:</strong> RESTful API per la comunicazione tra frontend e backend
            </ListGroup.Item>
            <ListGroup.Item>
              <strong>Gestione Stato:</strong> React Hooks (useState, useEffect) per la gestione dello stato
            </ListGroup.Item>
          </ListGroup>
        </Card.Body>
      </Card>

      <Alert variant="secondary" className="text-center">
        <p className="mb-0">
          Sviluppato per l'esame di Web 2 - Cybsercurity Specialist 2023/2025
        </p>
      </Alert>
    </Container>
  );
};

export default About;