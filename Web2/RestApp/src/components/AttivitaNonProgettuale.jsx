import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col } from 'react-bootstrap';
import axios from 'axios';

const AttivitaNonProgettuale = () => {
  const [attivita, setAttivita] = useState([]);
  const [attivitaFiltrate, setAttivitaFiltrate] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per memorizzare informazioni correlate sulle persone
  const [persone, setPersone] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Richiesta per le attività non progettuali
        const attivitaResponse = await axios.get(`http://localhost:8080/attivitanonprogettuale`);
        setAttivita(attivitaResponse.data);
        setAttivitaFiltrate(attivitaResponse.data);
        
        // Richiesta per le informazioni delle persone
        const personeResponse = await axios.get(`http://localhost:8080/persone`);
        const personeMap = {};
        personeResponse.data.forEach(persona => {
          personeMap[persona.id] = `${persona.nome} ${persona.cognome}`;
        });
        setPersone(personeMap);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };
    
    fetchData();
  }, []);

  useEffect(() => {
    filtrarAttivita();
  }, [tipoFiltro, valoreFiltro, attivita]);

  const filtrarAttivita = () => {
    if (tipoFiltro === 'all' || valoreFiltro === '') {
      setAttivitaFiltrate(attivita);
      return;
    }

    const filtered = attivita.filter(item => {
      const value = item[tipoFiltro];
      
      if (typeof value === 'number') {
        // Per campi numerici (id, persona, oreDurata)
        return value.toString().includes(valoreFiltro);
      } else {
        // Per campi di testo (tipo, giorno)
        return value.toLowerCase().includes(valoreFiltro.toLowerCase());
      }
    });
    
    setAttivitaFiltrate(filtered);
  };

  // Funzione per raggruppare le attività per tipo
  const getTipiAttivita = () => {
    const tipi = {};
    attivita.forEach(item => {
      if (!tipi[item.tipo]) {
        tipi[item.tipo] = 0;
      }
      tipi[item.tipo] += item.oreDurata;
    });
    return tipi;
  };

  // Calcolo delle statistiche
  const tipiAttivita = getTipiAttivita();

  return (
    <Container className="mt-4">
      <h1>Tabella Attività Non Progettuali</h1>
      
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
              <option value="persona">ID Persona</option>
              <option value="tipo">Tipo Attività</option>
              <option value="giorno">Data</option>
              <option value="oreDurata">Ore</option>
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
            <th>Persona</th>
            <th>Tipo Attività</th>
            <th>Data</th>
            <th>Ore</th>
          </tr>
        </thead>
        <tbody>
          {attivitaFiltrate.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{persone[item.persona] || item.persona}</td>
              <td>{item.tipo}</td>
              <td>{item.giorno}</td>
              <td>{item.oreDurata}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      <p>Totale attività visualizzate: {attivitaFiltrate.length} su {attivita.length}</p>

      {/* Statistiche dei tipi di attività */}
      <h3 className="mt-4">Riepilogo per Tipo di Attività</h3>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Tipo di Attività</th>
            <th>Ore Totali</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(tipiAttivita).map(([tipo, ore], index) => (
            <tr key={index}>
              <td>{tipo}</td>
              <td>{ore}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  );
};

export default AttivitaNonProgettuale;