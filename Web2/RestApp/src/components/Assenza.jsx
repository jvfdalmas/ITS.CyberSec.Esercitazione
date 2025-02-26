import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import './CustomTable.css'; 

const Assenze = () => {
  const [assenze, setAssenze] = useState([]);
  const [assenzeFiltrate, setAssenzeFiltrate] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per memorizzare informazioni correlate sulle persone
  const [persone, setPersone] = useState({});
  // Aggiungiamo un array con tutte le persone
  const [personeFull, setPersoneFull] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Richiesta per le assenze
        const assenzeResponse = await axios.get(`http://localhost:8080/assenze`);
        setAssenze(assenzeResponse.data);
        setAssenzeFiltrate(assenzeResponse.data);
        
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
    filtrarAssenze();
  }, [tipoFiltro, valoreFiltro, assenze, persone]);

  const filtrarAssenze = () => {
    if (tipoFiltro === 'all' || valoreFiltro === '') {
      setAssenzeFiltrate(assenze);
      return;
    }

    const filtered = assenze.filter(item => {
      if (tipoFiltro === 'persona') {
        // Cerca nel nome della persona invece che nell'ID
        const nomePersona = persone[item.persona] || "";
        return nomePersona.toLowerCase().includes(valoreFiltro.toLowerCase());
      } else {
        const value = item[tipoFiltro];
        
        if (typeof value === 'number') {
          // Per campi numerici (id)
          return value.toString().includes(valoreFiltro);
        } else {
          // Per campi di testo (tipo, giorno)
          return value.toLowerCase().includes(valoreFiltro.toLowerCase());
        }
      }
    });
    
    setAssenzeFiltrate(filtered);
  };

  // Funzione per raggruppare le assenze per tipo
  const getTipiAssenza = () => {
    const tipi = {};
    assenze.forEach(item => {
      if (!tipi[item.tipo]) {
        tipi[item.tipo] = 0;
      }
      tipi[item.tipo]++;
    });
    return tipi;
  };

  // Funzione per raggruppare le assenze per persona
  const getAssenzePerPersona = () => {
    const assenzePersona = {};
    assenze.forEach(item => {
      const personaId = item.persona;
      const personaNome = persone[personaId] || `Persona ID: ${personaId}`;
      
      if (!assenzePersona[personaNome]) {
        assenzePersona[personaNome] = 0;
      }
      assenzePersona[personaNome]++;
    });
    return assenzePersona;
  };

  // Calcolo delle statistiche
  const tipiAssenza = getTipiAssenza();
  const assenzePerPersona = getAssenzePerPersona();

  return (
    <Container className="mt-4">
      <h1>Tabella Assenze</h1>
      
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
              <option value="tipo">Tipo Assenza</option>
              <option value="giorno">Data</option>
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
            <th>Tipo Assenza</th>
            <th>Data</th>
          </tr>
        </thead>
        <tbody>
          {assenzeFiltrate.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{persone[item.persona] || item.persona}</td>
              <td>{item.tipo}</td>
              <td>{item.giorno}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      <p>Totale assenze visualizzate: {assenzeFiltrate.length} su {assenze.length}</p>

      {/* Statistiche e dashboard */}
      <h2 className="mt-5 mb-4">Riepilogo</h2>
      
      <Row>
        {/* Riepilogo per tipo di assenza */}
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Assenze per Tipologia</Card.Header>
            <Card.Body>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Tipo di Assenza</th>
                    <th>Conteggio</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(tipiAssenza).map(([tipo, conteggio], index) => (
                    <tr key={index}>
                      <td>{tipo}</td>
                      <td>{conteggio}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
        
        {/* Riepilogo per persona */}
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Assenze per Persona</Card.Header>
            <Card.Body>
              <Table striped bordered hover>
                <thead>
                  <tr>
                    <th>Persona</th>
                    <th>Numero Assenze</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(assenzePerPersona)
                    .sort((a, b) => b[1] - a[1]) // Ordina per numero di assenze (decrescente)
                    .map(([persona, conteggio], index) => (
                      <tr key={index}>
                        <td>{persona}</td>
                        <td>{conteggio}</td>
                      </tr>
                    ))}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Assenze;