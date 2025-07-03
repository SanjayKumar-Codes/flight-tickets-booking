import requests
import pandas as pd

def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()

        states = data.get("states", [])

        if not states:
            return pd.DataFrame()  # Empty dataframe if no data

        columns = [
            "icao24", "callsign", "origin_country", "time_position", "last_contact",
            "longitude", "latitude", "baro_altitude", "on_ground",
            "velocity", "true_track", "vertical_rate", "sensors",
            "geo_altitude", "squawk", "spi", "position_source"
        ]

        df = pd.DataFrame(states, columns=columns)
        return df

    except Exception as e:
        print(f"Error fetching flight data: {e}")
        return pd.DataFrame()
