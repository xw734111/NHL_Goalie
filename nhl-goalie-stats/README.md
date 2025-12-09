# NHL Goalie Stats Application

This project is a web application that provides statistics for NHL goalies using the NHL's REST API. It consists of a Flask backend that fetches and processes goalie data and a React frontend that displays this data to users.

## Project Structure

```
nhl-goalie-stats
├── backend
│   ├── app.py                # Main entry point for the Flask application
│   ├── api                   # Contains API routes
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services              # Contains services for interacting with the NHL API
│   │   ├── __init__.py
│   │   └── nhl_api.py
│   ├── models                # Contains data models
│   │   ├── __init__.py
│   │   └── goalie.py
│   ├── utils                 # Contains utility functions for data processing
│   │   ├── __init__.py
│   │   └── data_processor.py
│   ├── requirements.txt      # Python dependencies for the backend
│   └── config.py             # Configuration settings for the Flask application
├── frontend                  # Contains the React application
│   ├── public
│   │   └── index.html        # Main HTML file for the React application
│   ├── src
│   │   ├── App.js            # Main component of the React application
│   │   ├── index.js          # Entry point for the React application
│   │   ├── components        # Contains React components
│   │   │   ├── GoalieList.js
│   │   │   └── GoalieCard.js
│   │   ├── services          # Contains API call functions
│   │   │   └── api.js
│   │   └── styles            # Contains CSS styles
│   │       └── App.css
│   ├── package.json          # npm configuration file for the frontend
│   └── .gitignore            # Git ignore file for the frontend
├── README.md                 # Project documentation
└── .gitignore                # Git ignore file for the root directory
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python app.py
   ```

### Frontend

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the React application:
   ```
   npm start
   ```

## Usage

- Access the frontend application in your web browser at `http://localhost:3000`.
- The application will display a list of NHL goalies along with their statistics fetched from the backend.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is open-source and available under the MIT License.