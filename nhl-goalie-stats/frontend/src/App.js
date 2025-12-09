import React, { useEffect, useState } from 'react';
import './styles/App.css';
import GoalieList from './components/GoalieList';

function App() {
    const [goalies, setGoalies] = useState([]);

    useEffect(() => {
        const fetchGoalies = async () => {
            const response = await fetch('/api/goalies');
            const data = await response.json();
            setGoalies(data);
        };

        fetchGoalies();
    }, []);

    return (
        <div className="App">
            <h1>NHL Goalie Statistics</h1>
            <GoalieList goalies={goalies} />
        </div>
    );
}

export default App;