import React, { useState } from 'react';
import { Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';
import './Dashboard.css';
import { Link } from 'react-router-dom';

ChartJS.register(ArcElement, Tooltip, Legend);

const Dashboard = () => {
  const [selectedCell, setSelectedCell] = useState('5308'); // Default to Cell 5308

  const data = {
    5308: {
      labels: ['Healthy', 'Unhealthy'],
      datasets: [
        {
          data: [2992.02 / 3000 * 100, 100 - (2992.02 / 3000 * 100)],
          backgroundColor: ['#36A2EB', '#FF6384'],
          hoverBackgroundColor: ['#36A2EB', '#FF6384'],
        },
      ],
    },
    5329: {
      labels: ['Healthy', 'Unhealthy'],
      datasets: [
        {
          data: [2822.56 / 3000 * 100, 100 - (2822.56 / 3000 * 100)],
          backgroundColor: ['#36A2EB', '#FF6384'],
          hoverBackgroundColor: ['#36A2EB', '#FF6384'],
        },
      ],
    },
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 1, // Set aspect ratio to ensure the chart remains square
    plugins: {
      legend: {
        display: true,
        position: 'top',
      },
    },
  };

  const handleCellChange = (event) => {
    setSelectedCell(event.target.value);
  };

  return (
    <div className="dashboard-container">
      <div className="dropdown-container">
        <label htmlFor="cellSelect">Select Cell:</label>
        <select id="cellSelect" value={selectedCell} onChange={handleCellChange}>
          <option value="5308">Cell 5308</option>
          <option value="5329">Cell 5329</option>
        </select>
      </div>

      <div className="chart-section">
        <h2>Cell {selectedCell} State of Health</h2>
        <div className="chart-container">
          <Pie data={data[selectedCell]} options={options} />
        </div>
      </div>

      <div className="link-container">
        <Link to={`/cell/${selectedCell}`}>View Detailed Data for Cell {selectedCell}</Link>
      </div>
    </div>
  );
};

export default Dashboard;
