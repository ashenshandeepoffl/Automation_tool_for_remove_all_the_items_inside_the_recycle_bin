import time
import pyautogui

def empty_recycle_bin():
    # Open File Explorer
    pyautogui.hotkey('winleft', 'e')
    time.sleep(1)  # Wait for File Explorer to open

    # Focus on the address bar
    pyautogui.hotkey('alt', 'd')
    time.sleep(1)  # Wait for focus

    # Type the recycle bin path and press Enter
    pyautogui.write('::{645FF040-5081-101B-9F08-00AA002F954E}')
    pyautogui.press('enter')
    time.sleep(1)  # Wait for the recycle bin to open

    # Select all items in the recycle bin
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)  # Wait for items to be selected

    # Delete the selected items
    pyautogui.press('delete')
    time.sleep(1)  # Wait for confirmation dialog to appear

    # Confirm the deletion (press Enter)
    pyautogui.press('enter')
    time.sleep(1)  # Wait for deletion process to complete

    print("Recycle bin emptied successfully.")

if __name__ == "__main__":
    empty_recycle_bin()