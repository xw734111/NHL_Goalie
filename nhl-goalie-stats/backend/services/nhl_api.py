import requests
import pandas as pd

API_URL = "https://api.nhle.com/stats/rest/en/goalie/summary"

def fetch_goalie_stats():
    params = {
        "isAggregate": "false",
        "isGame": "false",
        "sort": '[{"property": "wins", "direction": "DESC"},'
                '{"property": "savePct", "direction": "DESC"},'
                '{"property": "playerId", "direction": "ASC"}]',
        "start": 0,
        "limit": 50,
        "cayenneExp": "gameTypeId = 2 and seasonId <=20242025"
    }

    headers = {"User-Agent": "Chrome/138.0"}

    response = requests.get(API_URL, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]
        return pd.DataFrame(data)
    else:
        response.raise_for_status()