import React from 'react';

const GoalieCard = ({ goalie }) => {
    return (
        <div className="goalie-card">
            <h2>{goalie.name}</h2>
            <p>Wins: {goalie.wins}</p>
            <p>Losses: {goalie.losses}</p>
            <p>Save Percentage: {goalie.savePct}</p>
            <p>Games Played: {goalie.gamesPlayed}</p>
        </div>
    );
};

export default GoalieCard;