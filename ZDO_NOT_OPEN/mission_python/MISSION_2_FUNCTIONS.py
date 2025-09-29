import pandas as pd


def load_dataframe(csv_path):
    """
    Loads a CSV file and checks if it's empty.
    """


    return data


def clean_data(data):
    """
    Cleans the dataset by removing missing values and duplicate rows.

    Args:
        df (pd.DataFrame): Raw DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """


    return df


def combine_data(list_of_dfs):
    """
    Combines a list of DataFrames into one.

    Args:
        list_of_dfs (list): List of DataFrames.

    Returns:
        pd.DataFrame: Combined DataFrame.
    """

    return combined


def aggregate_data(data):
    """
    Aggregates number of plays per artist, song, and month.
    Expected input contains one row per play.
    """
    # Group to get total plays per artist/song/month

    # Rename aggregated column to number_of_plays

    return df_grouped


def join_streams_with_revenue(stream_data, revenue_data):
    """
    Joins stream data with metadata on artist_id, song_name, and month.
    """


    return joined_df


def add_total_revenue(data):
    """
    Calculates total revenue = number_of_plays × revenue_per_play.
    """


    return data


def find_clue_1(data):
    """
    Calculates total global revenue from the joined dataset.
    """


    return total_revenue


def find_clue_2(data):
    """
    Finds the artist with the highest number of plays and returns their name and total revenue.
    """


    return total_revenue


def find_clue_3(data):
    """
    Finds the artist with the lowest total revenue in June and August and returns their total revenue.
    """


    return worst_revenue
