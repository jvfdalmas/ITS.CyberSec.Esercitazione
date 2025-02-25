import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CustomNavbar from './components/Navbar';
import Home from './components/Home';
import Persona from './components/Persona';
import Progetti from './components/Progetti';
import WPs from './components/WPs';
import AttivitaProgetto from './components/AttivitaProgetto';
import AttivitaNonProgettuale from './components/AttivitaNonProgettuale';
import Assenza from './components/Assenza';
import About from './components/About';

const App = () => {
  return (
    <Router>
      <CustomNavbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/persona" element={<Persona />} />
        <Route path="/progetti" element={<Progetti />} />
        <Route path="/WPS" element={<WPs />} />
        <Route path="/AttivitaProgetto" element={<AttivitaProgetto />} />
        <Route path="/AttivitaNonProgettuale" element={<AttivitaNonProgettuale />} />
        <Route path="/Assenza" element={<Assenza />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
};

export default App;