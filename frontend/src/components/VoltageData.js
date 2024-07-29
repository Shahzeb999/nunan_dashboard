import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const VoltageData = ({ cellId }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`/voltage_data/${cellId}`)
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching voltage data:', error));
  }, [cellId]);

  const chartData = {
    labels: data.map(d => `${d.cycle}-${d.step}`),
    datasets: [
      {
        label: 'Start Voltage',
        data: data.map(d => d.start_voltage),
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
      },
      {
        label: 'End Voltage',
        data: data.map(d => d.end_voltage),
        fill: false,
        backgroundColor: 'rgba(153,102,255,0.4)',
        borderColor: 'rgba(153,102,255,1)',
      },
    ],
  };

  return (
    <div>
      <h2>Voltage Data</h2>
      <Line data={chartData} />
    </div>
  );
};

export default VoltageData;
