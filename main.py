import pyautogui
import time
from pathlib import Path

# 5 seconds cooldown to allow user to terminate the program by moving the mouse to one of the 4 corners
time.sleep(5)

data_folder = Path("data/")
file_to_open = data_folder / "pangram.txt"
quotes = file_to_open.read_text().splitlines()

# make the text editor window active
pyautogui.click(300,1060)
for item in quotes:
    pyautogui.write(item)
    pyautogui.press('\n')
