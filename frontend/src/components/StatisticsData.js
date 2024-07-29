import React, { useEffect, useState } from 'react';
import { getStatisticsData } from '../api';

const StatisticsData = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getStatisticsData();
      setData(result);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>Statistics Data</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Channel</th>
            <th>Cycle</th>
            <th>Step</th>
            <th>Status</th>
            <th>Start Voltage</th>
            <th>End Voltage</th>
            <th>Start Current</th>
            <th>End Current</th>
            <th>Capacity</th>
            <th>Endure Time</th>
            <th>Relative Time</th>
            <th>Absolute Time</th>
            <th>Discharge Capacity 1</th>
            <th>Charge Capacity</th>
            <th>Discharge Capacity 2</th>
            <th>Net Energy Discharge</th>
            <th>Energy Charge</th>
            <th>Energy Discharge</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.channel}</td>
              <td>{item.cycle}</td>
              <td>{item.step}</td>
              <td>{item.status}</td>
              <td>{item.start_voltage}</td>
              <td>{item.end_voltage}</td>
              <td>{item.start_current}</td>
              <td>{item.end_current}</td>
              <td>{item.capacity}</td>
              <td>{item.endure_time}</td>
              <td>{item.relative_time}</td>
              <td>{item.absolute_time}</td>
              <td>{item.discharge_capacity_1}</td>
              <td>{item.charge_capacity}</td>
              <td>{item.discharge_capacity_2}</td>
              <td>{item.net_energy_discharge}</td>
              <td>{item.energy_charge}</td>
              <td>{item.energy_discharge}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StatisticsData;
