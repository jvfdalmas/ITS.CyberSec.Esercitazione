import React, { useState, useEffect } from 'react';
import { Toast, ToastContainer } from 'react-bootstrap';

const HomeAlert = () => {
  const [show, setShow] = useState(false);

  // Mostra il toast automaticamente all'avvio del componente
  useEffect(() => {
    setShow(true);
  }, []);

  return (
    <ToastContainer position="top-end" className="p-3">
      <Toast 
        show={show} 
        onClose={() => setShow(false)} 
        delay={30000} 
        autohide 
        className="border-0"
      >
        <Toast.Header className="bg-warning text-white">
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            width="20" 
            height="20" 
            fill="currentColor" 
            className="bi bi-exclamation-triangle-fill me-2" 
            viewBox="0 0 16 16" 
            role="img" 
            aria-label="Warning:"
          >
            <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
          </svg>
          <strong className="me-auto">Benvenuto in Accademia!</strong>
        </Toast.Header>
        <Toast.Body className="bg-light">
        Questa applicazione è stata sviluppata come progetto d'esame per il corso Web 2 - Cybersecurity Specialist 2023/2025.
        Il sistema combina un backend Flask con un frontend React per visualizzare i dati del database SQLite Accademia.
        </Toast.Body>
      </Toast>
    </ToastContainer>
  );
};

export default HomeAlert;