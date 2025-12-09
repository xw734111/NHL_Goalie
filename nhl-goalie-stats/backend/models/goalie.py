class Goalie:
    def __init__(self, player_id, name, wins, losses, save_percentage):
        self.player_id = player_id
        self.name = name
        self.wins = wins
        self.losses = losses
        self.save_percentage = save_percentage

    def __repr__(self):
        return f"Goalie({self.name}, Wins: {self.wins}, Losses: {self.losses}, Save Percentage: {self.save_percentage})"

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "save_percentage": self.save_percentage
        }