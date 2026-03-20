## Script by Hyker
## очень простенький макрос для удаления каналов в телеграмм в один клик!

import pyautogui
import keyboard
import time

# delete hotkey, хоткей удаления
HOTKEY = 'delete' 

def leave_telegram_chat():
    print("starting script... запускаем скрипт...")
    
    pyautogui.rightClick()
    
    time.sleep(0.5)
    
    pyautogui.press('up')
    time.sleep(0.2)
    
    pyautogui.press('enter')
    
    time.sleep(1.0) 
    
    pyautogui.press('enter') # пробуем
    time.sleep(0.5)
    pyautogui.press('enter') # если не получилось

    print("Successfully deleted!")

print(f"The script is active. Hover over the chat and click {HOTKEY.upper()}")

def trigger():
    leave_telegram_chat()
    time.sleep(1)

keyboard.add_hotkey(HOTKEY, trigger)

keyboard.wait()
