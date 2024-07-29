import React, { useState } from 'react';
import { uploadFile } from '../api';

const UploadPage = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (file) {
      const response = await uploadFile(file);
      setMessage(response.success || response.error);
    }
  };

  return (
    <div>
      <h1>Upload Data</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default UploadPage;
