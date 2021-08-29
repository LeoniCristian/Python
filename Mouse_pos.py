import time 
import win32api, win32con

while True:
    time.sleep(0.3)
    pos = win32api.GetCursorPos()
    print(pos)