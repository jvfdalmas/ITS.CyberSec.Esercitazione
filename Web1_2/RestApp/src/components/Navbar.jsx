import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './Navbar.css';

const CustomNavbar = () => {
  return (
    <Navbar bg="dark" variant="dark" expand="lg">
      <Container>
        <Navbar.Brand as={Link} to="/" className="text-white">Accademia</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/" className="custom-nav-link">Home</Nav.Link>
            <Nav.Link as={Link} to="/persona" className="custom-nav-link">Persone</Nav.Link>
            <Nav.Link as={Link} to="/progetti" className="custom-nav-link">Progetti</Nav.Link>
            <Nav.Link as={Link} to="/wps" className="custom-nav-link">WPs</Nav.Link>
            <Nav.Link as={Link} to="/attivitaprogetto" className="custom-nav-link">Attività Progetto</Nav.Link>
            <Nav.Link as={Link} to="/attivitanonprogettuale" className="custom-nav-link">Attività Non Progettuale</Nav.Link>
            <Nav.Link as={Link} to="/assenza" className="custom-nav-link">Assenze</Nav.Link>
            <Nav.Link as={Link} to="/about" className="custom-nav-link">About</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;