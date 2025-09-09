import os
import pyzipper

# Detect project root dynamically based on this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

mission_output_folder = os.path.join(project_root, "FINAL")
zip_output_file = os.path.join(mission_output_folder, "FINAL.zip")

# Create MISSION_1 folder if needed
os.makedirs(mission_output_folder, exist_ok=True)

# --- STEP 1: WRITE README FILE ---
readme_text = r"""                    
 _____ ______   ___  ________   ________  ___  ________  ________                               
|\   _ \  _   \|\  \|\   ____\ |\   ____\|\  \|\   __  \|\   ___  \                             
\ \  \\\__\ \  \ \  \ \  \___|_\ \  \___|\ \  \ \  \|\  \ \  \\ \  \                            
 \ \  \\|__| \  \ \  \ \_____  \\ \_____  \ \  \ \  \\\  \ \  \\ \  \                           
  \ \  \    \ \  \ \  \|____|\  \\|____|\  \ \  \ \  \\\  \ \  \\ \  \                          
   \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \__\ \_______\ \__\\ \__\                         
    \|__|     \|__|\|__|\_________|\_________\|__|\|_______|\|__| \|__|                         
                       \|_________\|_________|                                                  
                                                                                                
                                                                                                
 ________  ________  _____ ______   ________  ___       _______  _________  _______   ___       
|\   ____\|\   __  \|\   _ \  _   \|\   __  \|\  \     |\  ___ \|\___   ___|\  ___ \ |\  \      
\ \  \___|\ \  \|\  \ \  \\\__\ \  \ \  \|\  \ \  \    \ \   __/\|___ \  \_\ \   __/|\ \  \     
 \ \  \    \ \  \\\  \ \  \\|__| \  \ \   ____\ \  \    \ \  \_|/__  \ \  \ \ \  \_|/_\ \  \    
  \ \  \____\ \  \\\  \ \  \    \ \  \ \  \___|\ \  \____\ \  \_|\ \  \ \  \ \ \  \_|\ \ \__\   
   \ \_______\ \_______\ \__\    \ \__\ \__\    \ \_______\ \_______\  \ \__\ \ \_______\|__|   
    \|_______|\|_______|\|__|     \|__|\|__|     \|_______|\|_______|   \|__|  \|_______|   ___ 
                                                                                           |\__\
                                                                                           \|__|
                                                                                                
                                                                    

Agent, you absolutely smashed it.  
The data is clean, the code is cracked, and HQ is seriously impressed.  
Global Radio’s systems are running smoother than a DJ’s fade-out.

💥 Your prize? A classified stash of sweets from HQ’s *very* secret snack drawer.  
(Trust us… these don’t make it out often.)

You’ve officially gone from rookie to certified Data Agent.

— HQ Out.
"""

readme_path = os.path.join(project_root, "DO_NOT_OPEN/FINAL.txt")
with open(readme_path, "w", encoding='utf-8') as f:
    f.write(readme_text)

# --- Set zip password ---
clue1 = "1519"  # Replace with actual clue 1
clue2 = "449"  # Replace with actual clue 2
clue3 = "3"  # Replace with actual clue 3
password = f"{clue1}{clue2}{clue3}"
password_bytes = bytes(password, 'utf-8')

# --- Create encrypted zip ---
with pyzipper.AESZipFile(zip_output_file, 'w',
                         compression=pyzipper.ZIP_DEFLATED,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(password_bytes)

    # Add README
    zf.write(readme_path, arcname=f"FINAL/FINAL.txt")


print(f"✅ Encrypted zip created: {zip_output_file}")
