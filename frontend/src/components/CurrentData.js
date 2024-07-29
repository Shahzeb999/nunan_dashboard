import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { getCurrentData } from '../api';

const CurrentData = ({ cellId }) => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log(`Fetching data for cellId: ${cellId}`); // Log cellId
    getCurrentData(cellId)
      .then(response => {
        console.log('Fetched data:', response); // Log fetched data
        setData(response);
      })
      .catch(error => {
        console.error('Error fetching current data:', error);
        setError('Error fetching current data');
      });
  }, [cellId]);

  if (error) {
    return <div>{error}</div>;
  }

  const chartData = {
    labels: data.map(d => `${d.cycle}-${d.step}`),
    datasets: [
      {
        label: 'Current',
        data: data.map(d => d.cur),
        fill: false,
        backgroundColor: 'rgba(75,192,192,0.4)',
        borderColor: 'rgba(75,192,192,1)',
      }
    ],
  };

  return (
    <div>
      <h2>Current Data</h2>
      <Line data={chartData} />
    </div>
  );
};

export default CurrentData;
