import React, { useEffect, useState } from 'react';
import axios from 'axios';
import GoalieCard from './GoalieCard';

const GoalieList = () => {
    const [goalies, setGoalies] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchGoalies = async () => {
            try {
                const response = await axios.get('/api/goalies');
                setGoalies(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchGoalies();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error fetching goalies: {error.message}</div>;
    }

    return (
        <div className="goalie-list">
            {goalies.map((goalie) => (
                <GoalieCard key={goalie.playerId} goalie={goalie} />
            ))}
        </div>
    );
};

export default GoalieList;