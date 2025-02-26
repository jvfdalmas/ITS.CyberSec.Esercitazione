import React, { useEffect, useState } from 'react';
import { Container, Row, Col, Card, Button, Alert } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import axios from 'axios';
import HomeAlert from './HomeAlert';

const Home = () => {
  
  const [stats, setStats] = useState({
    persone: 0,
    progetti: 0,
    wps: 0,
    attivitaProgetto: 0,
    attivitaNonProgettuale: 0,
    assenze: 0
  });
  
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      setLoading(true);
      try {
        const [personeRes, progettiRes, wpsRes, attivitaProgettoRes, attivitaNonProgettualeRes, assenzeRes] = await Promise.all([
          axios.get('http://localhost:8080/persone'),
          axios.get('http://localhost:8080/progetti'),
          axios.get('http://localhost:8080/wps'),
          axios.get('http://localhost:8080/attivitaprogetto'),
          axios.get('http://localhost:8080/attivitanonprogettuale'),
          axios.get('http://localhost:8080/assenze')
        ]);
        
        setStats({
          persone: personeRes.data.length,
          progetti: progettiRes.data.length,
          wps: wpsRes.data.length,
          attivitaProgetto: attivitaProgettoRes.data.length,
          attivitaNonProgettuale: attivitaNonProgettualeRes.data.length,
          assenze: assenzeRes.data.length
        });
        
        setLoading(false);
      } catch (err) {
        console.error("Errore nel caricamento delle statistiche:", err);
        setError("Impossibile caricare le statistiche. Assicurati che il server sia in esecuzione.");
        setLoading(false);
      }
    };
    
    fetchStats();
  }, []);

  return (
    <Container fluid className="py-5 px-4" style={{ backgroundColor: '#f8f9fa' }}>
      <Row className="justify-content-center mb-2">
        <Col md={10} lg={8}>
          <div className="text-center mb-5">
            <h1 className="display-4 mb-3" style={{ color: '#2c3e50' }}>Accademia</h1>
            <p className="lead" style={{ color: '#34495e' }}>
              Benvenuti nella dashboard di Accademia.
              Esplora i nostri dati e scopri le statistiche del nostro sistema.
            </p>
          </div>
        </Col>
      </Row>

      {/* HomeAlert come toast indipendente */}
      <HomeAlert />

      {error && (
        <Row className="justify-content-center mb-4">
          <Col md={10} lg={8}>
            <Alert variant="danger">
              {error}
            </Alert>
          </Col>
        </Row>
      )}

      {loading ? (
        <Row className="justify-content-center">
          <Col md={6} className="text-center">
            <p>Caricamento statistiche...</p>
          </Col>
        </Row>
      ) : (
        <Row className="justify-content-center">
          <Col md={12}>
            <Row>
              <Col md={4} className="mb-4">
                <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', borderColor: '#e0e0e0' }}>
                  <Card.Body className="d-flex flex-column">
                    <div className="text-center mb-3">
                      <i className="fas fa-users" style={{ fontSize: '2.5rem', color: '#3498db' }}></i>
                    </div>
                    <Card.Title className="text-center mb-3">Persone</Card.Title>
                    <Card.Text className="text-center mb-4">
                      Gestisci il personale e visualizza informazioni sulle posizioni e gli stipendi.
                    </Card.Text>
                    <div className="text-center mt-auto">
                      <div className="mb-3">
                        <span className="display-6">{stats.persone}</span>
                        <span className="ms-2">Registrati</span>
                      </div>
                      <Link to="/persona">
                        <Button variant="outline-primary" className="rounded-pill px-4">
                          Visualizza Persone
                        </Button>
                      </Link>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
              
              <Col md={4} className="mb-4">
                <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', borderColor: '#e0e0e0' }}>
                  <Card.Body className="d-flex flex-column">
                    <div className="text-center mb-3">
                      <i className="fas fa-project-diagram" style={{ fontSize: '2.5rem', color: '#2ecc71' }}></i>
                    </div>
                    <Card.Title className="text-center mb-3">Progetti</Card.Title>
                    <Card.Text className="text-center mb-4">
                      Esplora i progetti attivi, con dettagli su date, budget e work packages correlati.
                    </Card.Text>
                    <div className="text-center mt-auto">
                      <div className="mb-3">
                        <span className="display-6">{stats.progetti}</span>
                        <span className="ms-2">Progetti</span>
                      </div>
                      <Link to="/progetti">
                        <Button variant="outline-success" className="rounded-pill px-4">
                          Gestisci Progetti
                        </Button>
                      </Link>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
              
              <Col md={4} className="mb-4">
                <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', borderColor: '#e0e0e0' }}>
                  <Card.Body className="d-flex flex-column">
                    <div className="text-center mb-3">
                      <i className="fas fa-tasks" style={{ fontSize: '2.5rem', color: '#9b59b6' }}></i>
                    </div>
                    <Card.Title className="text-center mb-3">Work Packages</Card.Title>
                    <Card.Text className="text-center mb-4">
                      Visualizza i work packages di ciascun progetto con relative tempistiche.
                    </Card.Text>
                    <div className="text-center mt-auto">
                      <div className="mb-3">
                        <span className="display-6">{stats.wps}</span>
                        <span className="ms-2">Totali</span>
                      </div>
                      <Link to="/wps">
                      <Button 
                        variant="outline-info" 
                        className="rounded-pill px-4" 
                        style={{ borderColor: '#9b59b6', color: '#9b59b6' }}
                        onMouseOver={(e) => {
                          e.currentTarget.style.backgroundColor = '#9b59b6';
                          e.currentTarget.style.color = 'white';
                        }}
                        onMouseOut={(e) => {
                          e.currentTarget.style.backgroundColor = 'transparent';
                          e.currentTarget.style.color = '#9b59b6';
                        }}
                        >
                          Esplora WPs
                        </Button>
                      </Link>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
            
            <Row className="mt-4">
              <Col md={4} className="mb-4">
                <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', borderColor: '#e0e0e0' }}>
                  <Card.Body className="d-flex flex-column">
                    <div className="text-center mb-3">
                      <i className="fas fa-clipboard-list" style={{ fontSize: '2.5rem', color: '#e74c3c' }}></i>
                    </div>
                    <Card.Title className="text-center mb-3">Attività di Progetto</Card.Title>
                    <Card.Text className="text-center mb-4">
                      Monitora le attività di progetto con dettagli su persone, progetti e ore lavorate.
                    </Card.Text>
                    <div className="text-center mt-auto">
                      <div className="mb-3">
                        <span className="display-6">{stats.attivitaProgetto}</span>
                        <span className="ms-2">Attività</span>
                      </div>
                      <Link to="/attivitaprogetto">
                        <Button variant="outline-danger" className="rounded-pill px-4">
                          Visualizza Attività
                        </Button>
                      </Link>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
              
              <Col md={4} className="mb-4">
                <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', borderColor: '#e0e0e0' }}>
                  <Card.Body className="d-flex flex-column">
                    <div className="text-center mb-3">
                      <i className="fas fa-clipboard-check" style={{ fontSize: '2.5rem', color: '#f39c12' }}></i>
                    </div>
                    <Card.Title className="text-center mb-3">Attività Non Progettuali</Card.Title>
                    <Card.Text className="text-center mb-4">
                      Tieni traccia delle attività non legate a progetti specifici come formazione o incontri.
                    </Card.Text>
                    <div className="text-center mt-auto">
                      <div className="mb-3">
                        <span className="display-6">{stats.attivitaNonProgettuale}</span>
                        <span className="ms-2">Registrate</span>
                      </div>
                      <Link to="/attivitanonprogettuale">
                        <Button variant="outline-warning" className="rounded-pill px-4">
                          Vedi Attività
                        </Button>
                      </Link>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
              
              <Col md={4} className="mb-4">
                <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', borderColor: '#e0e0e0' }}>
                  <Card.Body className="d-flex flex-column">
                    <div className="text-center mb-3">
                      <i className="fas fa-calendar-alt" style={{ fontSize: '2.5rem', color: '#1abc9c' }}></i>
                    </div>
                    <Card.Title className="text-center mb-3">Assenze</Card.Title>
                    <Card.Text className="text-center mb-4">
                      Visualizza e analizza le assenze del personale con statistiche dettagliate.
                    </Card.Text>
                    <div className="text-center mt-auto">
                      <div className="mb-3">
                        <span className="display-6">{stats.assenze}</span>
                        <span className="ms-2">Assenze</span>
                      </div>
                      <Link to="/assenza">
                        <Button variant="outline-info" className="rounded-pill px-4">
                          Gestisci Assenze
                        </Button>
                      </Link>
                    </div>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
          </Col>
        </Row>
      )}
      
    </Container>
  );
};

export default Home;