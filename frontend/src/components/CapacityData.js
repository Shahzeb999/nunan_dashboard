import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

const CapacityData = ({ cellId }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`/capacity_data/${cellId}`)
      .then(response => setData(response.data))
      .catch(error => console.error('Error fetching capacity data:', error));
  }, [cellId]);

  const chartData = {
    labels: data.map(d => `${d.cycle}-${d.step}`),
    datasets: [
      {
        label: 'Capacity',
        data: data.map(d => d.capacity),
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  return (
    <div>
      <h2>Capacity Data</h2>
      <Line data={chartData} />
    </div>
  );
};

export default CapacityData;
