import React from 'react';
import { Container, Card, ListGroup, Alert } from 'react-bootstrap';

const About = () => {
  return (
    <Container className="my-5">
      <h1 className="text-center mb-5">About - Dashboard Accademia</h1>
      <div class="alert alert-primary d-flex align-items-center" role="alert">
        <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
          <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
        </svg>
        <div>
          Questa applicazione è stata sviluppata come l'esame del corso Web 2 - Cybsercurity Specialist 2023/2025. 
          Il sistema integra un backend Flask con un frontend React per l'esibizione delle tabelle nella base dati Accademia.
        </div>
      </div>

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

    </Container>
  );
};

export default About;