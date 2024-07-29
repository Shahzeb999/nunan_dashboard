# Battery Data Dashboard

## Overview

Battery Data Dashboard is a web application designed to visualize battery health and performance metrics. The project includes a backend server to handle data processing and a frontend client to display the data in an intuitive and interactive way.

## Features

- Upload and process battery data files
- Visualize battery health using pie charts
- View detailed battery performance metrics such as current, voltage, capacity, and temperature over time
- Interactive charts for easy data analysis

## Project Structure

```
.
├── backend
│   ├── app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── utils.py
│   ├── data
│   ├── migrations
│   ├── run.py
│   └── requirements.txt
├── frontend
│   ├── public
│   ├── src
│   │   ├── api
│   │   │   └── api.js
│   │   ├── components
│   │   │   ├── CycleData.js
│   │   │   ├── Dashboard.js
│   │   │   ├── DetailTemperatureData.js
│   │   │   ├── DetailVoltageData.js
│   │   │   ├── StatisticsData.js
│   │   │   └── CurrentData.js
│   │   ├── pages
│   │   │   ├── CellPage.js
│   │   │   ├── HomePage.js
│   │   │   └── UploadPage.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── style.css
│   ├── .env
│   ├── package.json
│   └── README.md
├── .gitignore
└── README.md
```

## Prerequisites

- Node.js
- npm
- Python 3.x
- pip

## Backend Setup

1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```sh
   python run.py
   ```

The backend server will start on port 3000.

## Frontend Setup

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```

2. Install the required npm packages:
   ```sh
   npm install
   ```

3. Create a `.env` file in the frontend directory with the following content to set the frontend port:
   ```
   PORT=8080
   ```

4. Start the frontend development server:
   ```sh
   npm start
   ```

The frontend server will start on port 8080.

## Usage

1. Open your browser and navigate to `http://localhost:8080` to access the frontend.
2. Use the dashboard to view battery health and performance metrics.
3. Upload battery data files on the upload page to process and visualize new data.

## Libraries and Tools Used

### Backend
- Flask: Web framework for building the backend server
- SQLAlchemy: ORM for database management
- Pandas: Data manipulation and analysis

### Frontend
- React: JavaScript library for building user interfaces
- Chart.js: Library for creating charts
- React Chart.js 2: React wrapper for Chart.js
- Axios: Promise-based HTTP client for making requests to the backend API

## API Endpoints

### Backend API
- `GET /api/cycle_data`: Fetch cycle data
- `GET /api/statistics_data`: Fetch statistics data
- `GET /api/detail_voltage_data`: Fetch detailed voltage data
- `GET /api/detail_temperature_data`: Fetch detailed temperature data
- `GET /api/current_data/:cellId`: Fetch current data for a specific cell
- `POST /upload`: Upload a new battery data file for processing

## Additional Information

### .gitignore

Make sure to include the following paths in your `.gitignore` file to prevent unwanted files from being committed to the repository:

```
/backend/__pycache__/
/backend/instance/
/backend/*.pyc
/backend/.env
/frontend/node_modules/
/frontend/build/
/frontend/.env
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
