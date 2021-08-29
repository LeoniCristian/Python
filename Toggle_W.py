import keyboard
import time 
import win32api, win32con

def c():
    pos = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,pos[0],pos[1])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,pos[0],pos[1])
    
move = False
click = False

def onkeypress(event):
    global move,click
    if event.name == 'esc' or event.name == 'freccia giù':
        move = False
        click = False
    if event.name == 'freccia su':        
        move = True
        click = False
    if event.name == '-':
        move = False
        click = True
        
keyboard.on_press(onkeypress)

while True:
    while move:
        keyboard.press('w')
        time.sleep(0.5)
        keyboard.release('w')
    while click:
        c()
        time.sleep(0.1)
    time.sleep(0.3)