import os
import pyzipper

# Detect project root dynamically based on this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

raw_data_folder = os.path.join(project_root, "ZDO_NOT_OPEN/day_2_raw")
mission_code_folder = os.path.join(project_root, "ZDO_NOT_OPEN/mission_python")
mission_output_folder = os.path.join(project_root, "DAY_2")
zip_output_file = os.path.join(mission_output_folder, "MISSION_2.zip")

# Create MISSION_1 folder if needed
os.makedirs(mission_output_folder, exist_ok=True)

# --- STEP 1: WRITE README FILE ---
readme_text = """
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

readme_path = os.path.join(project_root, "ZDO_NOT_OPEN/MISSION_2.txt")
with open(readme_path, "w", encoding='utf-8') as f:
    f.write(readme_text)

# --- Set zip password ---
clue1 = "LORDE"  # Replace with actual clue 1
clue2 = "ROAR"  # Replace with actual clue 2
clue3 = "NOTE"  # Replace with actual clue 3
password = f"{clue1}{clue2}{clue3}".lower()
password_bytes = bytes(password, 'utf-8')

# --- Create encrypted zip ---
with pyzipper.AESZipFile(zip_output_file, 'w',
                         compression=pyzipper.ZIP_DEFLATED,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(password_bytes)

    # Add README
    zf.write(readme_path, arcname=f"DAY_2/MISSION_2.txt")

    # Add the two CSVs from day_2_raw
    for filename in ["revenue.csv", "june.csv", "july.csv", "august.csv"]:
        csv_path = os.path.join(raw_data_folder, filename)
        if os.path.exists(csv_path):
            zf.write(csv_path, arcname=f"DAY_2/{filename}")
        else:
            print(f"⚠️ Warning: {filename} not found in {raw_data_folder}.")

    # Add all files from mission_python directly into MISSION_2
    for file in os.listdir(mission_code_folder):
        full_path = os.path.join(mission_code_folder, file)
        if os.path.isfile(full_path):
            arcname = os.path.join("DAY_2", file)
            zf.write(full_path, arcname=arcname)

print(f"✅ Encrypted zip created: {zip_output_file}")
