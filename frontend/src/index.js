import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App'; // Import your main App component
import './styles.css'; // Import your main CSS file if needed
import { BrowserRouter } from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
