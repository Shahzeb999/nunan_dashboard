import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, PointElement, LinearScale, Title, Tooltip, Legend } from 'chart.js';
import { getDetailTemperatureData } from '../api';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend);

const TemperatureChart = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const result = await getDetailTemperatureData();
      const labels = result.map(item => item.relative_time);
      const temperatures = result.map(item => item.auxiliary_channel_temperature);

      setData({
        labels: labels,
        datasets: [
          {
            label: 'Temperature Data',
            data: temperatures,
            borderColor: 'rgba(255,99,132,1)',
            backgroundColor: 'rgba(255,99,132,0.2)',
          },
        ],
      });
    };
    fetchData();
  }, []);

  return <Line data={data} />;
};

export default TemperatureChart;
