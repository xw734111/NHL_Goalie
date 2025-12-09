import axios from 'axios';

const API_URL = 'http://localhost:5000/api/goalies';

export const fetchGoalies = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching goalie data:', error);
        throw error;
    }
};