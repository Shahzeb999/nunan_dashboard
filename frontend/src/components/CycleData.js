import React, { useEffect, useState } from 'react';
import { getCycleData } from '../api';

const CycleData = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getCycleData();
      setData(result);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>Cycle Data</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Channel</th>
            <th>Total Cycle</th>
            <th>Charge Capacity</th>
            <th>Discharge Capacity</th>
            <th>Cycle Life</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.channel}</td>
              <td>{item.total_cycle}</td>
              <td>{item.charge_capacity}</td>
              <td>{item.discharge_capacity}</td>
              <td>{item.cycle_life}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CycleData;
