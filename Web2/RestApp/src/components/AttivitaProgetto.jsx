import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import './CustomTable.css'; 

const AttivitaProgetto = () => {
  const [attivita, setAttivita] = useState([]);
  const [attivitaFiltrate, setAttivitaFiltrate] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per memorizzare informazioni correlate
  const [persone, setPersone] = useState({});
  const [progetti, setProgetti] = useState({});
  const [wps, setWPs] = useState({});
  
  // Per le statistiche di riepilogo
  const [statistiche, setStatistiche] = useState({
    totaleOre: 0,
    mediaDurataAttivita: 0,
    attivitaPerTipo: {},
    tipoAttivitaPiuFrequente: '',
    progettiConPiuAttivita: [],
    personePiuAttive: [],
    attivitaPerMese: {}
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Richiesta per le attività di progetto
        const attivitaResponse = await axios.get(`http://localhost:8080/attivitaprogetto`);
        setAttivita(attivitaResponse.data);
        setAttivitaFiltrate(attivitaResponse.data);
        
        // Richiesta per le informazioni correlate
        const personeResponse = await axios.get(`http://localhost:8080/persone`);
        const personeMap = {};
        personeResponse.data.forEach(persona => {
          personeMap[persona.id] = `${persona.nome} ${persona.cognome}`;
        });
        setPersone(personeMap);
        
        const progettiResponse = await axios.get(`http://localhost:8080/progetti`);
        const progettiMap = {};
        progettiResponse.data.forEach(progetto => {
          progettiMap[progetto.id] = progetto.nome;
        });
        setProgetti(progettiMap);
        
        const wpsResponse = await axios.get(`http://localhost:8080/wps`);
        const wpsMap = {};
        wpsResponse.data.forEach(wp => {
          wpsMap[wp.id] = wp.nome;
        });
        setWPs(wpsMap);

        // Calcola le statistiche una volta che tutti i dati sono disponibili
        calcolaStatistiche(attivitaResponse.data, personeMap, progettiMap);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };
    
    fetchData();
  }, []);

  useEffect(() => {
    filtrarAttivita();
  }, [tipoFiltro, valoreFiltro, attivita, persone, progetti, wps]);

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
      } else if (tipoFiltro === 'progetto') {
        // Cerca nel nome del progetto invece che nell'ID
        const nomeProgetto = progetti[item.progetto] || "";
        return nomeProgetto.toLowerCase().includes(valoreFiltro.toLowerCase());
      } else if (tipoFiltro === 'wp') {
        // Cerca nel nome del work package invece che nell'ID
        const nomeWP = wps[item.wp] || "";
        return nomeWP.toLowerCase().includes(valoreFiltro.toLowerCase());
      } else {
        const value = item[tipoFiltro];
        
        if (typeof value === 'number') {
          // Per campi numerici (id, oreDurata)
          return value.toString().includes(valoreFiltro);
        } else {
          // Per campi di testo (giorno, tipo)
          return value.toLowerCase().includes(valoreFiltro.toLowerCase());
        }
      }
    });
    
    setAttivitaFiltrate(filtered);
  };

  // Funzione per calcolare le statistiche
  const calcolaStatistiche = (dati, personeMap, progettiMap) => {
    if (!dati.length) return;

    // Calcola ore totali e media
    const totaleOre = dati.reduce((acc, item) => acc + item.oreDurata, 0);
    const mediaDurataAttivita = totaleOre / dati.length;

    // Calcola attività per tipo
    const attivitaPerTipo = {};
    dati.forEach(item => {
      if (!attivitaPerTipo[item.tipo]) {
        attivitaPerTipo[item.tipo] = {
          conteggio: 0,
          ore: 0
        };
      }
      attivitaPerTipo[item.tipo].conteggio++;
      attivitaPerTipo[item.tipo].ore += item.oreDurata;
    });

    // Trova il tipo di attività più frequente
    let tipoAttivitaPiuFrequente = '';
    let maxAttivita = 0;
    for (const tipo in attivitaPerTipo) {
      if (attivitaPerTipo[tipo].conteggio > maxAttivita) {
        maxAttivita = attivitaPerTipo[tipo].conteggio;
        tipoAttivitaPiuFrequente = tipo;
      }
    }

    // Calcola attività per progetto
    const attivitaPerProgetto = {};
    dati.forEach(item => {
      if (!attivitaPerProgetto[item.progetto]) {
        attivitaPerProgetto[item.progetto] = {
          nome: progettiMap[item.progetto] || `Progetto ${item.progetto}`,
          conteggio: 0,
          ore: 0
        };
      }
      attivitaPerProgetto[item.progetto].conteggio++;
      attivitaPerProgetto[item.progetto].ore += item.oreDurata;
    });

    // Trova i 3 progetti con più attività
    const progettiConPiuAttivita = Object.values(attivitaPerProgetto)
      .sort((a, b) => b.ore - a.ore)
      .slice(0, 3);

    // Calcola attività per persona
    const attivitaPerPersona = {};
    dati.forEach(item => {
      if (!attivitaPerPersona[item.persona]) {
        attivitaPerPersona[item.persona] = {
          nome: personeMap[item.persona] || `Persona ${item.persona}`,
          conteggio: 0,
          ore: 0
        };
      }
      attivitaPerPersona[item.persona].conteggio++;
      attivitaPerPersona[item.persona].ore += item.oreDurata;
    });

    // Trova le 3 persone più attive
    const personePiuAttive = Object.values(attivitaPerPersona)
      .sort((a, b) => b.ore - a.ore)
      .slice(0, 3);

    // Calcola attività per mese
    const attivitaPerMese = {};
    dati.forEach(item => {
      const data = new Date(item.giorno);
      const mese = data.toLocaleString('it-IT', { month: 'long', year: 'numeric' });
      
      if (!attivitaPerMese[mese]) {
        attivitaPerMese[mese] = {
          conteggio: 0,
          ore: 0
        };
      }
      attivitaPerMese[mese].conteggio++;
      attivitaPerMese[mese].ore += item.oreDurata;
    });

    setStatistiche({
      totaleOre,
      mediaDurataAttivita,
      attivitaPerTipo,
      tipoAttivitaPiuFrequente,
      progettiConPiuAttivita,
      personePiuAttive,
      attivitaPerMese
    });
  };

  return (
    <Container className="mt-4">
      <h1>Tabella Attività di Progetto</h1>
      
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
              <option value="progetto">Progetto</option>
              <option value="wp">Work Package</option>
              <option value="giorno">Data</option>
              <option value="tipo">Tipo Attività</option>
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
      
      <Table striped bordered hover responsive>
        <thead>
          <tr>
            <th>ID</th>
            <th>Persona</th>
            <th>Progetto</th>
            <th>Work Package</th>
            <th>Data</th>
            <th>Tipo</th>
            <th>Ore</th>
          </tr>
        </thead>
        <tbody>
          {attivitaFiltrate.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{persone[item.persona] || item.persona}</td>
              <td>{progetti[item.progetto] || item.progetto}</td>
              <td>{wps[item.wp] || item.wp}</td>
              <td>{item.giorno}</td>
              <td>{item.tipo}</td>
              <td>{item.oreDurata}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      <p>Totale attività visualizzate: {attivitaFiltrate.length} su {attivita.length}</p>
      <p>Totale ore visualizzate: {attivitaFiltrate.reduce((sum, item) => sum + item.oreDurata, 0)}</p>

      {/* Sezione Riepilogo */}
      <h2 className="mt-5 mb-4">Riepilogo e Statistiche</h2>
      
      <Row>
        {/* Statistiche generali */}
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Statistiche Generali</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <tbody>
                  <tr>
                    <th>Totale Ore</th>
                    <td>{statistiche.totaleOre}</td>
                  </tr>
                  <tr>
                    <th>Media Durata Attività</th>
                    <td>{statistiche.mediaDurataAttivita.toFixed(2)} ore</td>
                  </tr>
                  <tr>
                    <th>Tipo Attività Più Frequente</th>
                    <td>{statistiche.tipoAttivitaPiuFrequente}</td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
          
          {/* Progetti più attivi */}
          <Card className="mb-4">
            <Card.Header as="h5">Progetti con Più Attività</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <thead>
                  <tr>
                    <th>Progetto</th>
                    <th>Ore Totali</th>
                    <th>Num. Attività</th>
                  </tr>
                </thead>
                <tbody>
                  {statistiche.progettiConPiuAttivita.map((progetto, index) => (
                    <tr key={index}>
                      <td>{progetto.nome}</td>
                      <td>{progetto.ore}</td>
                      <td>{progetto.conteggio}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
        
        <Col md={6}>
          {/* Persone più attive */}
          <Card className="mb-4">
            <Card.Header as="h5">Persone Più Attive</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <thead>
                  <tr>
                    <th>Persona</th>
                    <th>Ore Totali</th>
                    <th>Num. Attività</th>
                  </tr>
                </thead>
                <tbody>
                  {statistiche.personePiuAttive.map((persona, index) => (
                    <tr key={index}>
                      <td>{persona.nome}</td>
                      <td>{persona.ore}</td>
                      <td>{persona.conteggio}</td>
                    </tr>
                  ))}
                </tbody>
              </Table>
            </Card.Body>
          </Card>
          
          {/* Attività per tipo */}
          <Card className="mb-4">
            <Card.Header as="h5">Dettaglio per Tipo di Attività</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <thead>
                  <tr>
                    <th>Tipo</th>
                    <th>Ore Totali</th>
                    <th>Num. Attività</th>
                  </tr>
                </thead>
                <tbody>
                  {Object.entries(statistiche.attivitaPerTipo).map(([tipo, dati], index) => (
                    <tr key={index}>
                      <td>{tipo}</td>
                      <td>{dati.ore}</td>
                      <td>{dati.conteggio}</td>
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

export default AttivitaProgetto;