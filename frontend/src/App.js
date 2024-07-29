import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import UploadPage from './pages/UploadPage';
import CycleData from './components/CycleData';
import StatisticsData from './components/StatisticsData';
import DetailVoltageData from './components/DetailVoltageData';
import DetailTemperatureData from './components/DetailTemperatureData';
import Dashboard from './components/Dashboard';  // New component for SoH pie charts
import CellPage from './pages/CellPage';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/upload" element={<UploadPage />} />
          <Route path="/cycle-data" element={<CycleData />} />
          <Route path="/statistics-data" element={<StatisticsData />} />
          <Route path="/detail-voltage-data" element={<DetailVoltageData />} />
          <Route path="/detail-temperature-data" element={<DetailTemperatureData />} />
          <Route path="/dashboard" element={<Dashboard />} /> {/* New route for dashboard */}
          <Route path="/cell/:cellId" element={<CellPage />} /> {/* Route for cell-specific pages */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
