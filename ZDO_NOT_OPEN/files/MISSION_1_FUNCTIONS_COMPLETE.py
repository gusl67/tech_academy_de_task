import pandas as pd

# STEP 1 – Load the data
def load_dataframe(file_path):
    """
    Loads a CSV file and checks if it's empty.
    """
    data = pd.read_csv(file_path)

    if data.empty:
        raise ValueError("This file is empty. Please check the input.")

    return data


# STEP 2 – Clean the data
def clean_dataframe(data):
    """
    Removes any rows with missing values and any exact duplicates.
    """
    data = data.dropna()           # Remove rows with missing values
    data = data.drop_duplicates()  # Remove duplicate rows
    return data


# STEP 3 – Combine multiple datasets
def combine_datasets(list_of_dfs):
    """
    Combines a list of dataframes into one big dataframe.
    """
    combined_data = pd.concat(list_of_dfs, ignore_index=True)
    return combined_data


# STEP 4 – Clue 1: Most common artist
def find_clue_1(data):
    """
    Finds the artist who appears the most in the data.
    """
    artist_counts = data['artist_name'].value_counts()
    most_common_artist = artist_counts.idxmax()
    return most_common_artist


# STEP 5 – Clue 2: Most played song on Capital in UK in June and August
def find_clue_2(data):
    """
    Finds the most played song on Capital in the UK for June and August.
    """
    # Filter the data to just what we need
    filtered_data = data[
        (data['radio_station'] == 'Capital') &
        (data['region'] == 'UK') &
        (data['month'].isin(['June', 'August']))
    ]

    if filtered_data.empty:
        return None

    song_counts = filtered_data['song_name'].value_counts()
    most_played_song = song_counts.idxmax()
    return most_played_song


# STEP 6 – Clue 3: Word from last letters of 4 specific artists
def find_clue_3(data):
    """
    Gets a 4-letter word from the last letters of artist names
    that streamed in 'ROW' region in July, sorted by most plays.
    """
    # Filter to only rows in ROW region in July
    clue_data = data[
        (data['region'] == 'ROW') &
        (data['month'] == 'July')
    ]

    # Count how many times each artist shows up
    artist_counts = {}
    for name in clue_data['artist_name']:
        if name not in artist_counts:
            artist_counts[name] = 1
        else:
            artist_counts[name] += 1

    # Sort artists by number of streams (from highest to lowest)
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)

    # Take the first 4 artists
    top_4_artists = sorted_artists[:4]

    # Get the last letter of each artist’s name
    last_letters = []
    for artist in top_4_artists:
        name = artist[0]
        last_letter = name[-1]
        last_letters.append(last_letter)

    # Join the letters into a word
    clue_word = ''.join(last_letters)

    return clue_word
