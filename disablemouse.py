import pyautogui
import pygetwindow as gw
import time
import random
import keyboard

console_window = gw.getWindowsWithTitle('Console')[0]
console_window.hide()

screen_width, screen_height = pyautogui.size()

while True:
    wait_time = random.randint(1, 120)
    time.sleep(wait_time)

    x = random.randint(0, screen_width - console_window.width)
    y = random.randint(0, screen_height - console_window.height)
    console_window.moveTo(x, y)

    while True:
        mx, my = pyautogui.position()
        
        if console_window.contains(mx, my):
            if pyautogui.mouseDown(button='left'):
                pyautogui.mouseUp(button='left')
        
        if keyboard.is_pressed('end'):    
            exit()

        time.sleep(0.1)
