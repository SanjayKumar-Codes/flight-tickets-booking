# import pandas as pd

# def process_flight_data(df: pd.DataFrame):
#     if df.empty:
#         return {}

#     # Clean callsign
#     df['callsign'] = df['callsign'].fillna("Unknown").str.strip()

#     # Count flights by origin country
#     country_counts = df['origin_country'].value_counts().to_dict()

#     # Count how many flights are on ground vs in air
#     on_ground_counts = df['on_ground'].value_counts().to_dict()

#     insights = {
#         "total_flights": len(df),
#         "flights_per_country": country_counts,
#         "on_ground_status": {
#             "on_ground": on_ground_counts.get(True, 0),
#             "in_air": on_ground_counts.get(False, 0)
#         }
#     }

#     return insights


import pandas as pd

def process_flight_data(df: pd.DataFrame):
    if df.empty:
        return {}

    df['callsign'] = df['callsign'].fillna("Unknown").str.strip()

    # Flights per country
    country_counts = df['origin_country'].value_counts().to_dict()

    # Flights on ground vs in air
    on_ground_counts = df['on_ground'].value_counts().to_dict()

    # High-demand regions based on longitude & latitude clustering (simple grid approximation)
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df = df.dropna(subset=['longitude', 'latitude'])

    # Create approximate grid by rounding coordinates
    df['grid_lon'] = (df['longitude'] // 5) * 5  # 5-degree grid
    df['grid_lat'] = (df['latitude'] // 5) * 5

    location_counts = df.groupby(['grid_lon', 'grid_lat']).size().sort_values(ascending=False).head(5)
    high_demand_locations = location_counts.reset_index().rename(columns={0: 'flight_count'})

    insights = {
        "total_flights": len(df),
        "flights_per_country": country_counts,
        "on_ground_status": {
            "on_ground": on_ground_counts.get(True, 0),
            "in_air": on_ground_counts.get(False, 0)
        },
        "high_demand_locations": high_demand_locations.to_dict(orient="records")
    }

    return insights
