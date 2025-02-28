import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col } from 'react-bootstrap';
import axios from 'axios';
import './CustomTable.css'; 

const AttivitaNonProgettuale = () => {
  const [attivita, setAttivita] = useState([]);
  const [attivitaFiltrate, setAttivitaFiltrate] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per memorizzare informazioni correlate sulle persone
  const [persone, setPersone] = useState({});
  const [personeFull, setPersoneFull] = useState([]);

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
        setPersoneFull(personeResponse.data);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };
    
    fetchData();
  }, []);

  useEffect(() => {
    filtrarAttivita();
  }, [tipoFiltro, valoreFiltro, attivita, persone]);

  const filtrarAttivita = () => {
    if (tipoFiltro === 'all' || valoreFiltro === '') {
      setAttivitaFiltrate(attivita);
      return;
    }

    const filtered = attivita.filter(item => {
      if (tipoFiltro === 'persona') {
        // Cerca nel nome della persona invece che nell'ID
        const nomePersona = persone[item.persona] || "";
        return nomePersona.toLowerCase().includes(valoreFiltro.toLowerCase());
      } else {
        const value = item[tipoFiltro];
        
        if (typeof value === 'number') {
          // Per campi numerici (id, oreDurata)
          return value.toString().includes(valoreFiltro);
        } else {
          // Per campi di testo (tipo, giorno)
          return value.toLowerCase().includes(valoreFiltro.toLowerCase());
        }
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

  // Funzione per raggruppare le attività per persona
  const getAttivitaPerPersona = () => {
    const attivitaPersona = {};
    attivita.forEach(item => {
      const personaId = item.persona;
      const personaNome = persone[personaId] || `Persona ID: ${personaId}`;
      
      if (!attivitaPersona[personaNome]) {
        attivitaPersona[personaNome] = 0;
      }
      attivitaPersona[personaNome] += item.oreDurata;
    });
    return attivitaPersona;
  };

  // Calcolo delle statistiche
  const tipiAttivita = getTipiAttivita();
  const attivitaPerPersona = getAttivitaPerPersona();

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
              <option value="persona">Persona</option>
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
      <p>Totale ore visualizzate: {attivitaFiltrate.reduce((sum, item) => sum + item.oreDurata, 0)}</p>

      <Row className="mt-4">
        <Col md={6}>
          {/* Statistiche dei tipi di attività */}
          <h3>Riepilogo per Tipo di Attività</h3>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Tipo di Attività</th>
                <th>Ore Totali</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(tipiAttivita)
                .sort((a, b) => b[1] - a[1]) // Ordina per ore (decrescente)
                .map(([tipo, ore], index) => (
                  <tr key={index}>
                    <td>{tipo}</td>
                    <td>{ore}</td>
                  </tr>
                ))}
            </tbody>
          </Table>
        </Col>

        <Col md={6}>
          {/* Statistiche per persona */}
          <h3>Riepilogo per Persona</h3>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Persona</th>
                <th>Ore Totali</th>
              </tr>
            </thead>
            <tbody>
              {Object.entries(attivitaPerPersona)
                .sort((a, b) => b[1] - a[1]) // Ordina per ore (decrescente)
                .map(([persona, ore], index) => (
                  <tr key={index}>
                    <td>{persona}</td>
                    <td>{ore}</td>
                  </tr>
                ))}
            </tbody>
          </Table>
        </Col>
      </Row>
    </Container>
  );
};

export default AttivitaNonProgettuale;