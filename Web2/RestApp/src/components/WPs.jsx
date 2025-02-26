import React, { useEffect, useState } from 'react';
import { Container, Table, Form, Row, Col } from 'react-bootstrap';
import axios from 'axios';

const WPs = () => {
  const [wps, setWPs] = useState([]);
  const [wpsFiltrati, setWPsFiltrati] = useState([]);
  const [tipoFiltro, setTipoFiltro] = useState('all');
  const [valoreFiltro, setValoreFiltro] = useState('');
  
  // Per memorizzare i nomi dei progetti da mostrare nella tabella
  const [progetti, setProgetti] = useState({});
  const [progettiFull, setProgettiFull] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Richiesta per i WPs
        const wpsResponse = await axios.get(`http://localhost:8080/wps`);
        setWPs(wpsResponse.data);
        setWPsFiltrati(wpsResponse.data);
        
        // Richiesta per i progetti per ottenere i nomi
        const progettiResponse = await axios.get(`http://localhost:8080/progetti`);
        // Creiamo un oggetto con id del progetto come chiave e nome come valore
        const progettiMap = {};
        progettiResponse.data.forEach(progetto => {
          progettiMap[progetto.id] = progetto.nome;
        });
        setProgetti(progettiMap);
        setProgettiFull(progettiResponse.data);
      } catch (error) {
        console.error("Error fetching data: ", error);
      }
    };
    
    fetchData();
  }, []);

  useEffect(() => {
    filtrarWPs();
  }, [tipoFiltro, valoreFiltro, wps, progetti]);

  const filtrarWPs = () => {
    if (tipoFiltro === 'all' || valoreFiltro === '') {
      setWPsFiltrati(wps);
      return;
    }

    const filtered = wps.filter(wp => {
      if (tipoFiltro === 'progetto') {
        // Cerca nel nome del progetto invece che nell'ID
        const nomeProgetto = progetti[wp.progetto] || "";
        return nomeProgetto.toLowerCase().includes(valoreFiltro.toLowerCase());
      } else {
        const value = wp[tipoFiltro];
        if (typeof value === 'number') {
          // Per campi numerici (id)
          return value.toString().includes(valoreFiltro);
        } else {
          // Per campi di testo (nome, inizio, fine)
          return value.toLowerCase().includes(valoreFiltro.toLowerCase());
        }
      }
    });
    
    setWPsFiltrati(filtered);
  };

  return (
    <Container className="mt-4">
      <h1>Tabella Work Packages (WPs)</h1>
      
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
              <option value="progetto">Progetto</option>
              <option value="nome">Nome WP</option>
              <option value="inizio">Data Inizio</option>
              <option value="fine">Data Fine</option>
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
            <th>Progetto</th>
            <th>Nome WP</th>
            <th>Data Inizio</th>
            <th>Data Fine</th>
          </tr>
        </thead>
        <tbody>
          {wpsFiltrati.map(wp => (
            <tr key={wp.id}>
              <td>{wp.id}</td>
              <td>{progetti[wp.progetto] || wp.progetto}</td>
              <td>{wp.nome}</td>
              <td>{wp.inizio}</td>
              <td>{wp.fine}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      <p>Totale WPs visualizzati: {wpsFiltrati.length} su {wps.length}</p>
    </Container>
  );
};

export default WPs;