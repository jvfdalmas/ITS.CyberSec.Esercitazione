import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import './CustomTable.css'; 

const Persona = () => {
  const [persone, setPersone] = useState([]);
  const [personeFiltrate, setPersoneFiltrate] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per le statistiche di riepilogo
  const [statistiche, setStatistiche] = useState({
    stipendioMedio: 0,
    stipendioTotale: 0,
    numeroPerPosizione: {},
    posizionePiùComune: '',
    stipendioMassimo: 0,
    stipendioMinimo: 0
  });

  useEffect(() => {
    const getPersone = async () => {
      try {
        const response = await axios.get(`http://localhost:8080/persone`);
        setPersone(response.data);
        setPersoneFiltrate(response.data);
        calcolaStatistiche(response.data);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };
    getPersone();
  }, []);

  useEffect(() => {
    filtrarPersone();
  }, [tipoFiltro, valoreFiltro, persone]);

  const filtrarPersone = () => {
    if (tipoFiltro === 'all' || valoreFiltro === '') {
      setPersoneFiltrate(persone);
      return;
    }

    const filtered = persone.filter(persona => {
      const value = persona[tipoFiltro];
      
      if (typeof value === 'number') {
        // Per campi numerici (id, stipendio)
        return value.toString().includes(valoreFiltro);
      } else {
        // Per campi di testo (nome, cognome, posizione)
        return value.toLowerCase().includes(valoreFiltro.toLowerCase());
      }
    });
    
    setPersoneFiltrate(filtered);
  };

  // Funzione per calcolare le statistiche
  const calcolaStatistiche = (dati) => {
    if (dati.length === 0) return;

    // Calcola stipendio medio
    const stipendioTotale = dati.reduce((acc, persona) => acc + persona.stipendio, 0);
    const stipendioMedio = stipendioTotale / dati.length;

    // Conta persone per posizione
    const conteggioPosizioni = {};
    dati.forEach(persona => {
      conteggioPosizioni[persona.posizione] = (conteggioPosizioni[persona.posizione] || 0) + 1;
    });

    // Trova la posizione più comune
    let posizionePiùComune = '';
    let maxCount = 0;
    for (const [posizione, conteggio] of Object.entries(conteggioPosizioni)) {
      if (conteggio > maxCount) {
        maxCount = conteggio;
        posizionePiùComune = posizione;
      }
    }

    // Trova stipendio massimo e minimo
    const stipendi = dati.map(persona => persona.stipendio);
    const stipendioMassimo = Math.max(...stipendi);
    const stipendioMinimo = Math.min(...stipendi);

    setStatistiche({
      stipendioMedio,
      stipendioTotale,
      numeroPerPosizione: conteggioPosizioni,
      posizionePiùComune,
      stipendioMassimo,
      stipendioMinimo
    });
  };

  return (
    <Container className="mt-4">
      <h1>Tabella Persona</h1>
      
      <Row className="mb-3">
        <Col md={4}>
          <Form.Group controlId="tipoFiltroSelect">
            <Form.Label>Filtra per campo:</Form.Label>
            <Form.Select 
              value={tipoFiltro} 
              onChange={(e) => setTipoFiltro(e.target.value)}
            >
              <option value="all">Tutti i campi</option>
              <option value="id">ID</option>
              <option value="nome">Nome</option>
              <option value="cognome">Cognome</option>
              <option value="posizione">Posizione</option>
              <option value="stipendio">Stipendio</option>
            </Form.Select>
          </Form.Group>
        </Col>
        
        <Col md={8}>
          <Form.Group controlId="valoreFiltro">
            <Form.Label>Valore filtro:</Form.Label>
            <Form.Control 
              type="text" 
              placeholder="Inserisci il valore da cercare..."
              value={valoreFiltro}
              onChange={(e) => setValoreFiltro(e.target.value)}
            />
          </Form.Group>
        </Col>
      </Row>
      
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Cognome</th>
            <th>Posizione</th>
            <th>Stipendio</th>
          </tr>
        </thead>
        <tbody>
          {personeFiltrate.map(persona => (
            <tr key={persona.id}>
              <td>{persona.id}</td>
              <td>{persona.nome}</td>
              <td>{persona.cognome}</td>
              <td>{persona.posizione}</td>
              <td>{persona.stipendio.toLocaleString('it-IT')} €</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      <p>Totale persone visualizzate: {personeFiltrate.length} su {persone.length}</p>

      {/* Sezione Riepilogo */}
      <h2 className="mt-5 mb-4">Riepilogo e Statistiche</h2>
      
      <Row>
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Statistiche Stipendi</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <tbody>
                  <tr>
                    <th>Stipendio Medio</th>
                    <td>{statistiche.stipendioMedio.toLocaleString('it-IT', { maximumFractionDigits: 2 })} €</td>
                  </tr>
                  <tr>
                    <th>Stipendio Totale</th>
                    <td>{statistiche.stipendioTotale.toLocaleString('it-IT')} €</td>
                  </tr>
                  <tr>
                    <th>Stipendio Massimo</th>
                    <td>{statistiche.stipendioMassimo.toLocaleString('it-IT')} €</td>
                  </tr>
                  <tr>
                    <th>Stipendio Minimo</th>
                    <td>{statistiche.stipendioMinimo.toLocaleString('it-IT')} €</td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
        
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Distribuzione per Posizione</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <thead>
                  <tr>
                    <th>Posizione</th>
                    <th>Numero di Persone</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(statistiche.numeroPerPosizione).map(([posizione, numero], index) => (
                    <tr key={index}>
                      <td>{posizione}</td>
                      <td>{numero}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
              <p className="mt-3 mb-0">
                <strong>Posizione più comune:</strong> {statistiche.posizionePiùComune}
              </p>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Persona;