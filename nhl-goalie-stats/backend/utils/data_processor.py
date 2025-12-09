def process_goalie_data(data):
    # Convert the raw data into a more usable format
    processed_data = []
    for goalie in data:
        processed_goalie = {
            "name": goalie.get("fullName"),
            "team": goalie.get("teamName"),
            "wins": goalie.get("wins"),
            "losses": goalie.get("losses"),
            "save_percentage": goalie.get("savePct"),
            "goals_against_average": goalie.get("gaa"),
        }
        processed_data.append(processed_goalie)
    return processed_data

def clean_data(df):
    # Clean the DataFrame by removing any rows with missing values
    return df.dropna()