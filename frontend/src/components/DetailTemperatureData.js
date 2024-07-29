import React, { useEffect, useState } from 'react';
import { getDetailTemperatureData } from '../api'; // Ensure to import the API function

function DetailTemperatureData() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getDetailTemperatureData();
      setData(result);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>Detail Temperature Data</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Record ID</th>
            <th>Step Name</th>
            <th>Relative Time</th>
            <th>Realtime</th>
            <th>Auxiliary Channel Temperature</th>
            <th>Gap of Temperature</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row) => (
            <tr key={row.id}>
              <td>{row.id}</td>
              <td>{row.record_id}</td>
              <td>{row.step_name}</td>
              <td>{row.relative_time}</td>
              <td>{row.realtime}</td>
              <td>{row.auxiliary_channel_temperature}</td>
              <td>{row.gap_of_temperature}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DetailTemperatureData;
