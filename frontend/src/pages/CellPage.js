import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Line, Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import './CellPage.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const CellPage = () => {
  const { cellId } = useParams();
  const [currentData, setCurrentData] = useState([]);
  const [voltageData, setVoltageData] = useState([]);
  const [capacityData, setCapacityData] = useState([]);
  const [temperatureData, setTemperatureData] = useState([]);
  const [timeData, setTimeData] = useState([]);

  useEffect(() => {
    // Fetch data from the backend based on the cellId
    fetch(`http://127.0.0.1:3000/api/cell-data/${cellId}`)
      .then(response => response.json())
      .then(data => {
        setCurrentData(data.currentData);
        setVoltageData(data.voltageData);
        setCapacityData(data.capacityData);
        setTemperatureData(data.temperatureData);
        setTimeData(data.timeData);
      });
  }, [cellId]);

  const currentChartData = {
    labels: timeData,
    datasets: [
      {
        label: 'Current (mA)',
        data: currentData,
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
      },
    ],
  };

  const voltageChartData = {
    labels: timeData,
    datasets: [
      {
        label: 'Voltage (V)',
        data: voltageData,
        borderColor: 'rgba(153, 102, 255, 1)',
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
      },
    ],
  };

  const capacityChartData = {
    labels: timeData,
    datasets: [
      {
        label: 'Capacity (mAh)',
        data: capacityData,
        borderColor: 'rgba(255, 159, 64, 1)',
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
      },
    ],
  };

  const temperatureChartData = {
    labels: timeData,
    datasets: [
      {
        label: 'Temperature (°C)',
        data: temperatureData,
        borderColor: 'rgba(255, 99, 132, 1)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        type: 'category',
      },
      y: {
        beginAtZero: true,
      },
    },
    plugins: {
      legend: {
        display: true,
        position: 'top',
      },
      title: {
        display: true,
        text: 'Cell Data',
      },
    },
  };

  return (
    <div className="cell-page-container">
      <h1>Cell {cellId} Data</h1>
      <div className="chart-section">
        <h2>Current Data</h2>
        <div className="chart-container">
          <Line data={currentChartData} options={options} />
        </div>
      </div>
      <div className="chart-section">
        <h2>Voltage Data</h2>
        <div className="chart-container">
          <Line data={voltageChartData} options={options} />
        </div>
      </div>
      <div className="chart-section">
        <h2>Capacity Data</h2>
        <div className="chart-container">
          <Bar data={capacityChartData} options={options} />
        </div>
      </div>
      <div className="chart-section">
        <h2>Temperature Data</h2>
        <div className="chart-container">
          <Line data={temperatureChartData} options={options} />
        </div>
      </div>
    </div>
  );
};

export default CellPage;
