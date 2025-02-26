import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';
import './CustomTable.css'; 

const Progetti = () => {
  const [progetti, setProgetti] = useState([]);
  const [progettiFiltrati, setProgettiFiltrati] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per le statistiche di riepilogo
  const [statistiche, setStatistiche] = useState({
    budgetTotale: 0,
    budgetMedio: 0,
    budgetMassimo: 0,
    budgetMinimo: 0,
    progettiInCorso: 0,
    progettiCompletati: 0,
    progettiPianificati: 0,
    durataMediaGiorni: 0
  });

  useEffect(() => {
    const getProgetti = async () => {
      try {
        const response = await axios.get(`http://localhost:8080/progetti`);
        setProgetti(response.data);
        setProgettiFiltrati(response.data);
        calcolaStatistiche(response.data);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };
    getProgetti();
  }, []);

  useEffect(() => {
    filtrarProgetti();
  }, [tipoFiltro, valoreFiltro, progetti]);

  const filtrarProgetti = () => {
    if (tipoFiltro === 'all' || valoreFiltro === '') {
      setProgettiFiltrati(progetti);
      return;
    }

    const filtered = progetti.filter(progetto => {
      const value = progetto[tipoFiltro];
      
      if (typeof value === 'number') {
        // Per campi numerici (id, budget)
        return value.toString().includes(valoreFiltro);
      } else {
        // Per campi di testo (nome, inizio, fine)
        return value.toLowerCase().includes(valoreFiltro.toLowerCase());
      }
    });
    
    setProgettiFiltrati(filtered);
  };

  // Funzione per calcolare le statistiche dei progetti
  const calcolaStatistiche = (dati) => {
    if (dati.length === 0) return;

    // Calcola budget totale e medio
    const budgetTotale = dati.reduce((acc, progetto) => acc + progetto.budget, 0);
    const budgetMedio = budgetTotale / dati.length;

    // Trova budget massimo e minimo
    const budgets = dati.map(progetto => progetto.budget);
    const budgetMassimo = Math.max(...budgets);
    const budgetMinimo = Math.min(...budgets);

    // Conta progetti per stato
    const oggi = new Date();
    let progettiInCorso = 0;
    let progettiCompletati = 0;
    let progettiPianificati = 0;
    let durataTotaleGiorni = 0;

    dati.forEach(progetto => {
      const dataInizio = new Date(progetto.inizio);
      const dataFine = new Date(progetto.fine);
      
      // Calcola la durata in giorni
      const durataGiorni = Math.round((dataFine - dataInizio) / (1000 * 60 * 60 * 24));
      durataTotaleGiorni += durataGiorni;
      
      // Determina lo stato del progetto
      if (oggi < dataInizio) {
        progettiPianificati++;
      } else if (oggi > dataFine) {
        progettiCompletati++;
      } else {
        progettiInCorso++;
      }
    });

    const durataMediaGiorni = durataTotaleGiorni / dati.length;

    setStatistiche({
      budgetTotale,
      budgetMedio,
      budgetMassimo,
      budgetMinimo,
      progettiInCorso,
      progettiCompletati,
      progettiPianificati,
      durataMediaGiorni
    });
  };

  // Funzione per ottenere il budget totale dei progetti filtrati
  const getBudgetTotaleFiltered = () => {
    return progettiFiltrati.reduce((acc, progetto) => acc + progetto.budget, 0);
  };

  return (
    <Container className="mt-4">
      <h1>Tabella Progetti</h1>
      
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
              <option value="inizio">Data Inizio</option>
              <option value="fine">Data Fine</option>
              <option value="budget">Budget</option>
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
            <th>Nome Progetto</th>
            <th>Data Inizio</th>
            <th>Data Fine</th>
            <th>Budget (€)</th>
          </tr>
        </thead>
        <tbody>
          {progettiFiltrati.map(progetto => (
            <tr key={progetto.id}>
              <td>{progetto.id}</td>
              <td>{progetto.nome}</td>
              <td>{progetto.inizio}</td>
              <td>{progetto.fine}</td>
              <td>{progetto.budget.toLocaleString('it-IT')}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      <p>Totale progetti visualizzati: {progettiFiltrati.length} su {progetti.length}</p>
      <p>Budget totale dei progetti visualizzati: {getBudgetTotaleFiltered().toLocaleString('it-IT')} €</p>

      {/* Sezione Riepilogo */}
      <h2 className="mt-5 mb-4">Riepilogo e Statistiche</h2>
      
      <Row>
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Statistiche Budget</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <tbody>
                  <tr>
                    <th>Budget Totale</th>
                    <td>{statistiche.budgetTotale.toLocaleString('it-IT')} €</td>
                  </tr>
                  <tr>
                    <th>Budget Medio</th>
                    <td>{statistiche.budgetMedio.toLocaleString('it-IT', { maximumFractionDigits: 2 })} €</td>
                  </tr>
                  <tr>
                    <th>Budget Massimo</th>
                    <td>{statistiche.budgetMassimo.toLocaleString('it-IT')} €</td>
                  </tr>
                  <tr>
                    <th>Budget Minimo</th>
                    <td>{statistiche.budgetMinimo.toLocaleString('it-IT')} €</td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
        
        <Col md={6}>
          <Card className="mb-4">
            <Card.Header as="h5">Statistiche Progetti</Card.Header>
            <Card.Body>
              <Table striped bordered>
                <tbody>
                  <tr>
                    <th>Progetti in Corso</th>
                    <td>{statistiche.progettiInCorso}</td>
                  </tr>
                  <tr>
                    <th>Progetti Completati</th>
                    <td>{statistiche.progettiCompletati}</td>
                  </tr>
                  <tr>
                    <th>Progetti Pianificati</th>
                    <td>{statistiche.progettiPianificati}</td>
                  </tr>
                  <tr>
                    <th>Durata Media (giorni)</th>
                    <td>{Math.round(statistiche.durataMediaGiorni)}</td>
                  </tr>
                </tbody>
              </Table>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Progetti;