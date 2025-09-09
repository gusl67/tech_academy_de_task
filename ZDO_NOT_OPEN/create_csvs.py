import pandas as pd
import random
from faker import Faker
from datetime import datetime, date

fake = Faker()

# Constants
regions = ['UK', 'US', 'ROW']
radio_stations = ['Capital', 'Gold', 'Heart', 'Smooth', "Classic_FM"]

artists = [
    {"artist_id": 1, "artist_name": "Taylor Swift", "songs": ["Love Story", "You Belong With Me", "Shake It Off"]},
    {"artist_id": 2, "artist_name": "Ed Sheeran", "songs": ["Shape of You", "Perfect", "Thinking Out Loud"]},
    {"artist_id": 3, "artist_name": "Adele", "songs": ["Hello", "Rolling in the Deep", "Someone Like You"]},
    {"artist_id": 4, "artist_name": "Drake", "songs": ["God's Plan", "In My Feelings", "Hotline Bling"]},
    {"artist_id": 5, "artist_name": "Billie Eilish", "songs": ["Bad Guy", "Ocean Eyes", "When The Party's Over"]},
    {"artist_id": 6, "artist_name": "The Weeknd", "songs": ["Blinding Lights", "Starboy", "Can't Feel My Face"]},
    {"artist_id": 7, "artist_name": "Dua Lipa", "songs": ["Levitating", "Don't Start Now", "New Rules"]},
    {"artist_id": 8, "artist_name": "Bruno Mars", "songs": ["Uptown Funk", "Just The Way You Are", "24K Magic"]},
    {"artist_id": 9, "artist_name": "Ariana Grande", "songs": ["7 Rings", "Thank U, Next", "No Tears Left To Cry"]},
    {"artist_id": 10, "artist_name": "Post Malone", "songs": ["Circles", "Sunflower", "Rockstar"]},
    {"artist_id": 11, "artist_name": "Imagine Dragons", "songs": ["Believer", "Thunder", "Radioactive"]},
    {"artist_id": 12, "artist_name": "Shawn Mendes", "songs": ["Stitches", "Treat You Better", "In My Blood"]},
    {"artist_id": 13, "artist_name": "Lady Gaga", "songs": ["Poker Face", "Bad Romance", "Shallow"]},
    {"artist_id": 14, "artist_name": "Katy Perry", "songs": ["Firework", "Roar", "Dark Horse"]},
    {"artist_id": 15, "artist_name": "Coldplay", "songs": ["Yellow", "Fix You", "Viva La Vida"]},
    {"artist_id": 16, "artist_name": "Zara Larsson", "songs": ["Lush Life", "Symphony", "Ruin My Life"]},
    {"artist_id": 17, "artist_name": "Lorde", "songs": ["Royals", "Green Light", "Solar Power"]},
    {"artist_id": 18, "artist_name": "Rosalia", "songs": ["Malamente", "Pienso En Tu Mirá", "Con Altura"]},
    {"artist_id": 19, "artist_name": "SZA", "songs": ["Good Days", "The Weekend", "Love Galore"]},
    {"artist_id": 20, "artist_name": "Demi Lovato", "songs": ["Cool for the Summer", "Confident", "Heart Attack"]},
]


def create_dataset(month, year, n=100, duplicate_prob=0.15, null_row_prob=0.05):
    rows = []

    month_name = {6: "June", 7: "July", 8: "August"}[month]
    month_days = {6: 30, 7: 31, 8: 31}[month]

    forced_rows = []

    def random_date():
        day = random.randint(1, month_days)
        return date(year, month, day)

    # Ensure Lorde is most common across all months
    lorde = next(a for a in artists if a["artist_name"] == "Lorde")
    for _ in range(25):
        forced_rows.append({
            'date': random_date(),
            'month': month_name,
            'artist_id': lorde["artist_id"],
            'artist_name': lorde["artist_name"],
            'song_name': random.choice(lorde["songs"]),
            'radio_station': random.choice(radio_stations),
            'region': random.choice(['UK', 'US'])
        })

    # Ensure Roar plays on Capital UK in June & August
    if month in [6, 8]:
        katy = next(a for a in artists if a["artist_name"] == "Katy Perry")
        for _ in range(15):
            forced_rows.append({
                'date': random_date(),
                'month': month_name,
                'artist_id': katy["artist_id"],
                'artist_name': katy["artist_name"],
                'song_name': "Roar",
                'radio_station': "Capital",
                'region': "UK"
            })

    # Special case for July – only these 4 artists in ROW
    if month == 7:
        target_artists = {
            "Zara Larsson": 15,
            "Demi Lovato": 8,
            "Taylor Swift": 6,
            "Lorde": 3
        }
        for name, count in target_artists.items():
            a = next(art for art in artists if art["artist_name"] == name)
            for _ in range(count):
                forced_rows.append({
                    'date': random_date(),
                    'month': month_name,
                    'artist_id': a["artist_id"],
                    'artist_name': a["artist_name"],
                    'song_name': random.choice(a["songs"]),
                    'radio_station': random.choice(radio_stations),
                    'region': "ROW"
                })

    for row in forced_rows:
        rows.append(row)
        if random.random() < duplicate_prob:
            rows.append(row.copy())

    while len(rows) < n:
        if random.random() < null_row_prob:
            rows.append({
                'date': None,
                'month': None,
                'artist_id': None,
                'artist_name': None,
                'song_name': None,
                'radio_station': None,
                'region': None
            })
            continue

        artist = random.choice(artists)

        if month == 7:
            if artist["artist_name"] in ["Lorde", "Zara Larsson", "Taylor Swift", "Demi Lovato"]:
                region = random.choice(regions)
            else:
                region = random.choice(['UK', 'US'])
        else:
            region = random.choice(regions)

        row = {
            'date': random_date(),
            'month': month_name,
            'artist_id': artist["artist_id"],
            'artist_name': artist["artist_name"],
            'song_name': random.choice(artist["songs"]),
            'radio_station': random.choice(radio_stations),
            'region': region
        }

        rows.append(row)
        if random.random() < duplicate_prob:
            rows.append(row.copy())

    return pd.DataFrame(rows[:n])



# Generate datasets
df_june = create_dataset(6, 2024, 100)
df_july = create_dataset(7, 2024, 100)
df_august = create_dataset(8, 2024, 100)

# Save CSVs
df_june.to_csv('june.csv', index=False)
df_july.to_csv('july.csv', index=False)
df_august.to_csv('august.csv', index=False)

print("✅ CSVs created: june.csv, july.csv, august.csv")

# --- Bonus analysis: Last letters of artists not in UK/US in July
non_uk_us = df_july[
    (df_july['region'].notna()) &
    (~df_july['region'].str.upper().isin(['UK', 'US'])) &
    (df_july['artist_name'].notna())
]

# Only unique artists in non-UK/US
unique_artists = non_uk_us['artist_name'].dropna().unique()
last_letters = sorted(set(a.strip()[-1] for a in unique_artists))[:4]

print("🎯 Last letters of the only 4 artists who streamed outside UK/US in July:")
print(last_letters)
