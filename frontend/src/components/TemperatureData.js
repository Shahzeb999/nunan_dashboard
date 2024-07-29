import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const TemperatureData = ({ cellId }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`/temperature_data/${cellId}`)
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching temperature data:', error));
  }, [cellId]);

  const chartData = {
    labels: data.map(d => `${d.relative_time}`),
    datasets: [
      {
        label: 'Auxiliary Channel Temperature',
        data: data.map(d => d.auxiliary_channel_temperature),
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
      },
      {
        label: 'Gap of Temperature',
        data: data.map(d => d.gap_of_temperature),
        fill: false,
        backgroundColor: 'rgba(153,102,255,0.4)',
        borderColor: 'rgba(153,102,255,1)',
      },
    ],
  };

  return (
    <div>
      <h2>Temperature Data</h2>
      <Line data={chartData} />
    </div>
  );
};

export default TemperatureData;
