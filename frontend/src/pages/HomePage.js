import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to the Data Dashboard</h1>
      <ul>
        <li><Link to="/dashboard">Dashboard</Link></li>
        <li><Link to="/upload">Upload Data</Link></li>
        <li><Link to="/cycle-data">Cycle Data</Link></li>
        <li><Link to="/statistics-data">Statistics Data</Link></li>
        <li><Link to="/detail-voltage-data">Detail Voltage Data</Link></li>
        <li><Link to="/detail-temperature-data">Detail Temperature Data</Link></li>
      </ul>
    </div>
  );
};

export default HomePage;
