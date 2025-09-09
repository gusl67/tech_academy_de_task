import logging
from DO_NOT_OPEN.file_utils import combination_lock_2
from DAY_2.MISSION_2_FUNCTIONS import *

"""
 _____ ______   ___  ________   ________  ___  ________  ________           ________  ________  ___  _______   ________ 
|\   _ \  _   \|\  \|\   ____\ |\   ____\|\  \|\   __  \|\   ___  \        |\   __  \|\   __  \|\  \|\  ___ \ |\  _____\
\ \  \\\__\ \  \ \  \ \  \___|_\ \  \___|\ \  \ \  \|\  \ \  \\ \  \       \ \  \|\ /\ \  \|\  \ \  \ \   __/|\ \  \__/ 
 \ \  \\|__| \  \ \  \ \_____  \\ \_____  \ \  \ \  \\\  \ \  \\ \  \       \ \   __  \ \   _  _\ \  \ \  \_|/_\ \   __\
  \ \  \    \ \  \ \  \|____|\  \\|____|\  \ \  \ \  \\\  \ \  \\ \  \       \ \  \|\  \ \  \\  \\ \  \ \  \_|\ \ \  \_|
   \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \__\ \_______\ \__\\ \__\       \ \_______\ \__\\ _\\ \__\ \_______\ \__\ 
    \|__|     \|__|\|__|\_________|\_________\|__|\|_______|\|__| \|__|        \|_______|\|__|\|__|\|__|\|_______|\|__| 
                       \|_________\|_________|                                                                          
                                                                                                                        
                                                                                                                        
 ________  ________      ___    ___       _______                                                                       
|\   ___ \|\   __  \    |\  \  /  /|     /  ___  \                                                                      
\ \  \_|\ \ \  \|\  \   \ \  \/  / /    /__/|_/  /|                                                                     
 \ \  \ \\ \ \   __  \   \ \    / /     |__|//  / /                                                                     
  \ \  \_\\ \ \  \ \  \   \/  /  /          /  /_/__  ___ ___ ___                                                       
   \ \_______\ \__\ \__\__/  / /           |\________|\__|\__|\__\                                                      
    \|_______|\|__|\|__|\___/ /             \|_______\|__\|__\|__|                                                      
                       \|___|/                                             

🎯 Objective: Build a working data pipeline to uncover a hidden numerical code...

🎤 "Agents — yesterday you cleaned corrupted archives and uncovered a hidden message. But that was just the beginning."

📡 Global Radio’s database is broken and incomplete.

🚨 This morning, our systems intercepted fresh transmissions — external revenue data....

⚠️ These files are riddled with duplicates and rogue values that could crash the system.

🔐 Hidden somewhere inside this chaos is a secret numerical code — your only way to unlock the encrypted final zip file.  
Without it, Global Radio’s broadcast will be offline... forever.

👾 Your mission: clean, transform, and align the data — then crack the code before it’s too late.

💻 All functions are in `MISSION_2_FUNCTIONS.py`. Some are blanks waiting for your code wizardry.

🎉 Good luck, Agent — Global Radio is counting on you!
"""

# --- STEP 1: EXTRACT ---
# Load original Day 1 stream data
june_data = load_dataframe(csv_path="june.csv")
july_data = load_dataframe(csv_path="july.csv")
aug_data = load_dataframe(csv_path="august.csv")

# Load new metadata file with artist_id, revenue, plays
revenue_data = load_dataframe(csv_path="")

# --- STEP 2: TRANSFORM ---
june_clean = clean_data(data=june_data)
july_clean = clean_data(data=july_data)
aug_clean  = clean_data(data=aug_data)
revenue_clean = clean_data(data=revenue_data)

# Combine all monthly data
combined_streams = combine_data(list_of_dfs=[june_clean, july_clean, aug_clean])

# Calculate number of plays
aggregate_df = aggregate_data(data=combined_streams)

# Join revenue data on artist_name, song_name, and month
join_data = join_streams_with_revenue(stream_data=aggregate_df, revenue_data=revenue_data)
enriched_data_revenue = add_total_revenue(data=join_data)

# Clue 1: What is the total Global Revenue?
clue_1 = find_clue_1(data=enriched_data_revenue)
logging.info(f"Clue 1: {clue_1}")

# Clue 2: Find the artist with the highest number of plays and returns their name and total revenue?
clue_2 = find_clue_2(data=enriched_data_revenue)
logging.info(f"Clue 2: {clue_2}")

# Clue 3: Find the artist with the lowest total revenue in June and August and returns their total revenue?
clue_3 = find_clue_3(data=enriched_data_revenue)
logging.info(f"Clue 3: {clue_3}")

# Attempt to unlock the Prize file!
combination_lock_2(clue_1=str(clue_1),
                   clue_2=str(clue_2),
                   clue_3=str(clue_3))
