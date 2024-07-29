import axios from 'axios';

const API_URL = 'http://127.0.0.1:3000'; // Ensure this URL is correct

export const getCycleData = async () => {
  const response = await axios.get(`${API_URL}/cycle_data`);
  return response.data;
};

export const getStatisticsData = async () => {
  const response = await axios.get(`${API_URL}/statistics_data`);
  return response.data;
};

export const getDetailVoltageData = async () => {
  const response = await axios.get(`${API_URL}/detail_voltage_data`);
  return response.data;
};

export const getDetailTemperatureData = async () => {
  const response = await axios.get(`${API_URL}/detail_temperature_data`);
  return response.data;
};

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await axios.post(`${API_URL}/upload`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  return response.data;
};

export const getCurrentData = async (cellId) => {
  const response = await axios.get(`${API_URL}/current_data/${cellId}`);
  console.log(`Requesting URL: ${API_URL}/current_data/${cellId}`); // Log request URL
  return response.data;
};
