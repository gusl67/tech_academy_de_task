import pandas as pd

"""
Fill in the blanks in the code below to complete the functions.
"""

# STEP 1 – Load the data
def load_dataframe(file_path):
    """
    Loads a CSV file and checks if it's empty.
    """
    data = "*INSERT CODE HERE*"                           # Load the CSV file into a DataFrame

    if "*INSERT CODE HERE*":                              # Check if the DataFrame is empty and raise an error if it is.
        raise ValueError("This file is empty. Please check the input.")

    return data


# STEP 2 – Clean the data
def clean_dataframe(data):
    """
    Removes any rows with missing values and any exact duplicates.
    """
    data = "*INSERT CODE HERE*"                                    # Remove rows with missing values
    data = "*INSERT CODE HERE*"                                    # Remove duplicate rows
    return data


# STEP 3 – Combine multiple datasets
def combine_datasets(list_of_dfs):
    """
    Combines a list of dataframes into one big dataframe.
    """
    combined_data = "*INSERT CODE HERE*"(list_of_dfs, ignore_index=True) # Concatenate all dataframes in the list

    return combined_data


# STEP 4 – Clue 1: Most common artist
def find_clue_1(data):
    """
    Finds the artist who appears the most in the data.
    """
    artist_counts = "*INSERT CODE HERE*"                    # Count how many times each artist shows up
    most_common_artist = "*INSERT CODE HERE*"               # Sort artists by number of streams (from highest to lowest)

    return most_common_artist


# STEP 5 – Clue 2: Most played song on Capital in UK in June and August
def find_clue_2(data):
    """
    Finds the most played song on Capital in the UK for June and August.
    """
    filtered_data = "*INSERT CODE HERE*"                    # Filter to only rows in UK region in June and August

    if "*INSERT CODE HERE*":                                # Check if filtered data is empty
        return None

    song_counts = "*INSERT CODE HERE*"                      # Count how many times each song shows up
    most_played_song = "*INSERT CODE HERE*"                 # Sort songs by number of plays (from highest to lowest)

    return most_played_song


# STEP 6 – Clue 3: Word from last letters of 4 specific artists
def find_clue_3(data):
    """
    Gets a 4-letter word from the last letters of artist names
    who were the most played in July not in the UK or US.
    """
    clue_data = "*INSERT CODE HERE*"                        # Filter to only rows to not US or UK region in July

    artist_counts = {}                                      # Used count how many times each artist shows up
    for "*INSERT CODE HERE*" in "*INSERT CODE HERE*":       # Iterate through each row in the filtered data
        if "*INSERT CODE HERE*" not in "*INSERT CODE HERE*": # Check if the artist is already in the dictionary
            "*INSERT CODE HERE*"                            # If not, add it with a count of 1
        else:
            "*INSERT CODE HERE*"                            # If it is, increase the count by 1

                                                            # Sort artists by number of streams (from highest to lowest)
    sorted_artists = sorted(artist_counts.items(), key=lambda x: x[1], reverse=True)

    top_4_artists = "*INSERT CODE HERE*"                    # Get the top 4 artists

    last_letters = []                                       # List to hold the last letters of the artist names
    for "*INSERT CODE HERE*" in "*INSERT CODE HERE*":       # Iterate through the top 4 artists
        name = "*INSERT CODE HERE*"                         # Get the artist's name
        last_letter = "*INSERT CODE HERE*"                  # Get the last letter of the artist's name
        "*INSERT CODE HERE*"                                # Add the last letter to the list

    clue_word = "*INSERT CODE HERE*"                        # Join the last letters to form a word

    return clue_word
