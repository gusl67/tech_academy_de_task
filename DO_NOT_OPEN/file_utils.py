import pyzipper
import time
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def combination_lock_1(clue_1, clue_2, clue_3):
    """
    Unlocks DAY_2/DAY_2.zip using the provided clues as the password.
    Prints README and extracts all files into DAY_2/ directory.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    password = f"{clue_1}{clue_2}{clue_3}"
    logging.info(f"TRYING PASSWORD: {password}...")

    zip_path = os.path.join(project_root, "DAY_2/MISSION_2.zip")

    password = password.lower()

    try:
        with pyzipper.AESZipFile(zip_path) as zf:
            zf.pwd = password.encode("utf-8")

            # Print README if present
            if 'DAY_2/MISSION_2.txt' in zf.namelist():
                readme_text = zf.read('DAY_2/MISSION_2.txt').decode()
                logging.info("✅ PASSWORD CORRECT!.... PRINTING NEXT MISSION ✅\n")
                for char in readme_text:
                    print(char, end='', flush=True)
                    time.sleep(0.01)
                print()

            # Extract all files to output_folder
            for file_name in zf.namelist():
                output_path = os.path.join(project_root, file_name)
                with open(output_path, 'wb') as f_out:
                    f_out.write(zf.read(file_name))
                logging.info(f"📁 Extracted: {file_name} → {output_path}")


        # Delete the zip file after extraction
        zip_path = os.path.join(project_root, "DAY_2/MISSION_2.zip")
        os.remove(zip_path)
        logging.info(f"🗑️ Deleted zip file: {zip_path}")

    except RuntimeError:
        logging.warning("❌ INCORRECT PASSWORD! ACCESS DENIED ❌")
    except FileNotFoundError:
        logging.error("❌ Zip file not found.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


def combination_lock_2(clue_1, clue_2, clue_3):
    """
    Unlocks DAY_2/DAY_2.zip using the provided clues as the password.
    Prints README and extracts all files into DAY_2/ directory.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    password = f"{clue_1}{clue_2}{clue_3}"
    logging.info(f"TRYING PASSWORD: {password}...")

    zip_path = os.path.join(project_root, "FINAL/FINAL.zip")

    password = password.lower()

    try:
        with pyzipper.AESZipFile(zip_path) as zf:
            zf.pwd = password.encode("utf-8")

            # Print README if present
            if 'FINAL/FINAL.txt' in zf.namelist():
                readme_text = zf.read('FINAL/FINAL.txt').decode()
                logging.info("✅ PASSWORD CORRECT!.... CONGRATULATIONS ✅\n")
                for char in readme_text:
                    print(char, end='', flush=True)
                    time.sleep(0.01)
                print()

        # Extract all files to output_folder
        for file_name in zf.namelist():
            output_path = os.path.join(project_root, file_name)
            with open(output_path, 'wb') as f_out:
                f_out.write(zf.read(file_name))
            logging.info(f"📁 Extracted: {file_name} → {output_path}")

        # Delete the zip file after extraction
        zip_path = os.path.join(project_root, "FINAL/FINAL.zip")
        os.remove(zip_path)
        logging.info(f"🗑️ Deleted zip file: {zip_path}")

    except RuntimeError:
        logging.warning("❌ INCORRECT PASSWORD! ACCESS DENIED ❌")
    except FileNotFoundError:
        logging.error("❌ Zip file not found.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")