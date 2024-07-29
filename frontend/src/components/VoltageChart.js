import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, LineElement, PointElement, LinearScale, Title, Tooltip, Legend } from 'chart.js';
import { getDetailVoltageData } from '../api';

ChartJS.register(LineElement, PointElement, LinearScale, Title, Tooltip, Legend);

const VoltageChart = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const result = await getDetailVoltageData();
      const labels = result.map(item => item.relative_time);
      const voltages = result.map(item => item.auxiliary_channel_voltage);

      setData({
        labels: labels,
        datasets: [
          {
            label: 'Voltage Data',
            data: voltages,
            borderColor: 'rgba(75,192,192,1)',
            backgroundColor: 'rgba(75,192,192,0.2)',
          },
        ],
      });
    };
    fetchData();
  }, []);

  return <Line data={data} />;
};

export default VoltageChart;
