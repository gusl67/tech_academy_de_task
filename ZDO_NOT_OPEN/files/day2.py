import pandas as pd


def load_dataframe(csv_path):
    """
    Loads a CSV file and checks if it's empty.
    """
    data = pd.read_csv(csv_path)

    if data.empty:
        raise ValueError("This file is empty. Please check the input.")

    return data


def clean_data(data):
    """
    Cleans the dataset by removing missing values and duplicate rows.

    Args:
        df (pd.DataFrame): Raw DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = data.dropna()

    df = df.drop_duplicates()

    return df


def combine_data(list_of_dfs):
    """
    Combines a list of DataFrames into one.

    Args:
        list_of_dfs (list): List of DataFrames.

    Returns:
        pd.DataFrame: Combined DataFrame.
    """
    combined = pd.concat(list_of_dfs, ignore_index=True)
    return combined


def aggregate_data(data):
    """
    Aggregates number of plays per artist, song, and month.
    Expected input contains one row per play.
    """
    # Group to get total plays per artist/song/month
    df_grouped = data.groupby(
        ['artist_id', 'song_name', 'month'],
        as_index=False
    ).size()

    # Rename aggregated column to number_of_plays
    df_grouped = df_grouped.rename(columns={'size': 'number_of_plays'})

    return df_grouped


def join_streams_with_revenue(stream_data, revenue_data):
    """
    Joins stream data with metadata on artist_id, song_name, and month.
    """
    stream_df_indexed = stream_data.set_index(['artist_id', 'song_name', 'month'])
    revenue_df_indexed = revenue_data.set_index(['artist_id', 'song_name', 'month'])
    joined_df = stream_df_indexed.join(revenue_df_indexed, how='left', rsuffix='_meta').reset_index()
    return joined_df


def add_total_revenue(data):
    """
    Calculates total revenue = number_of_plays × revenue_per_play.
    """
    data['total_revenue'] = data['number_of_plays'] * data['revenue_per_play_gbp']

    return data


def find_clue_1(data):
    """
    Calculates total global revenue from the joined dataset.
    """
    total_revenue = int(data['total_revenue'].sum())

    return total_revenue


def find_clue_2(data):
    """
    Finds the artist with the highest number of plays and returns their total revenue.
    """
    top_artist = data.groupby('artist_id')['number_of_plays'].sum().idxmax()

    total_revenue = int(data[data['artist_id'] == top_artist]['total_revenue'].sum())

    return total_revenue


def find_clue_3(data):
    """
    Finds the artist with the lowest total revenue in June and August and returns their total revenue.
    """
    filtered = data[data['month'].isin(['June', 'August'])]

    revenue_by_artist = filtered.groupby('artist_id')['total_revenue'].sum()

    worst_revenue = int(revenue_by_artist.min())

    return worst_revenue
