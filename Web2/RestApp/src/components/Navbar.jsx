import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const CustomNavbar = () => {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand as={Link} to="/">Accademia</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">Home</Nav.Link>
            <Nav.Link as={Link} to="/persona">Persone</Nav.Link>
            <Nav.Link as={Link} to="/progetti">Progetti</Nav.Link>
            <Nav.Link as={Link} to="/wps">WPs</Nav.Link>
            <Nav.Link as={Link} to="/attivitaprogetto">Attività Progetto</Nav.Link>
            <Nav.Link as={Link} to="/attivitanonprogettuale">Attività Non Progettuale</Nav.Link>
            <Nav.Link as={Link} to="/assenza">Assenze</Nav.Link>
            <Nav.Link as={Link} to="/about">About</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default CustomNavbar;