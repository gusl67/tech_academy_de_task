import logging
from ZDO_NOT_OPEN.file_utils import combination_lock_1
from DAY_1.MISSION_1_FUNCTIONS import *

"""
 _____ ______   ___  ________   ________  ___  ________  ________           ________  ________  ___  _______   ________ 
|\   _ \  _   \|\  \|\   ____\ |\   ____\|\  \|\   __  \|\   ___  \        |\   __  \|\   __  \|\  \|\  ___ \ |\  _____\
\ \  \\\__\ \  \ \  \ \  \___|_\ \  \___|\ \  \ \  \|\  \ \  \\ \  \       \ \  \|\ /\ \  \|\  \ \  \ \   __/|\ \  \__/ 
 \ \  \\|__| \  \ \  \ \_____  \\ \_____  \ \  \ \  \\\  \ \  \\ \  \       \ \   __  \ \   _  _\ \  \ \  \_|/_\ \   __\
  \ \  \    \ \  \ \  \|____|\  \\|____|\  \ \  \ \  \\\  \ \  \\ \  \       \ \  \|\  \ \  \\  \\ \  \ \  \_|\ \ \  \_|
   \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \__\ \_______\ \__\\ \__\       \ \_______\ \__\\ _\\ \__\ \_______\ \__\ 
    \|__|     \|__|\|__|\_________|\_________\|__|\|_______|\|__| \|__|        \|_______|\|__|\|__|\|__|\|_______|\|__| 
                       \|_________\|_________|                                                                          
                                                                                                                        
                                                                                                                        
 ________  ________      ___    ___       _____                                                                         
|\   ___ \|\   __  \    |\  \  /  /|     / __  \                                                                        
\ \  \_|\ \ \  \|\  \   \ \  \/  / /    |\/_|\  \                                                                       
 \ \  \ \\ \ \   __  \   \ \    / /     \|/ \ \  \                                                                      
  \ \  \_\\ \ \  \ \  \   \/  /  /           \ \  \                                                                     
   \ \_______\ \__\ \__\__/  / /              \ \__\                                                                    
    \|_______|\|__|\|__|\___/ /                \|__|                                                                    
                       \|___|/                                                                                                                                                                              
                                                                                        
You’re the newest Junior Data Engineer at Global Radio, and the system’s in lockdown.
Streaming data from June, July, and August is a total mess — duplicates, missing info, and chaos everywhere.  
Without fixing this, Global Radio’s airwaves stay silent.

🎯 Your mission: clean the chaos, combine the data, and unlock the clues hidden deep in the noise.  
🔓 Only by cracking these clues can you reboot the system and get the next set of intel to restore Global Radio.

🛠️ Your task:  
    1️⃣ Load messy monthly CSVs using `load_dataframe()`  
    2️⃣ Clean them with `clean_dataframe()` (remove missing values + duplicates)  
    3️⃣ Combine into one dataset with `combine_datasets()`  
    4️⃣ Crack 3 clues using `find_clue_1()`, `find_clue_2()`, and `find_clue_3()`  

🕵️ The clues will test your pipeline:  
    🎤 Clue 1: Most common artist overall  
    🎵 Clue 2: Top song on Capital (UK, June & August only)  
    🎶 Clue 3: Musical word from the 4 top artists streamed outside UK & US in July  

🔑 Only when you enter all 3 clues correctly into `combination_lock(clue_1, clue_2, clue_3)` will Global Radio’s next transmission unlock.

💻 Your code and skills are the key. Get the system back online — the company depends on you.

📂 All functions you need are in `MISSION_1_FUNCTIONS.py` — most are blank and waiting for your logic.
"""

# STEP 1 – Load Your Data
df_june = load_dataframe("MISSION_1_DATA/june.csv")
df_july = load_dataframe("MISSION_1_DATA/july.csv")
df_august = load_dataframe("MISSION_1_DATA/august.csv")


# STEP 2 - Clean Data
df_june = clean_dataframe(data=df_june)
df_july = clean_dataframe(data=df_july)
df_aug = clean_dataframe(data=df_august)


# STEP 3 – Combine the Datasets
combined_data = combine_datasets(list_of_dfs=[df_june, df_july, df_august])


# STEP 4 – Clue 1: Most common artist that appears in the dataset?
clue_1 = find_clue_1(data=combined_data)
logging.info(f"Clue 1: {clue_1}")


# STEP 5 – Clue 2: Most common song played on Capital in the UK for June and August?
clue_2 = find_clue_2(data=combined_data)
logging.info(f"Clue 2: {clue_2}")


# STEP 6 – Clue 3: Musical word made up of last letters of the only 4 artists that got streams not in the UK or US,
#                  in July, ordered by number of streams descending?
clue_3 = find_clue_3(data=combined_data)
logging.info(f"Clue 3: {clue_3}")


# STEP 7 – Combine clues to unlock the combination lock, run the script to try it out!
combination_lock_1(clue_1=clue_1,
                   clue_2=clue_2,
                   clue_3=clue_3)


