import time 
import win32api, win32con
import Beep as B
import ctypes

def pomodoro(work=25,rest=5,final=True):
    B.beep(bp_freq=200,bp_time=1000)
    time.sleep(60*work)

    B.beep(clock_freq=5,clock_time=1000,bp_freq=-1,bp_time=100)
    time.sleep(60*rest)
    if(final):
        #B.beep(bp_freq=2000,bp_time=1000)
        B.play_song(B.ZELDA)
        ctypes.windll.user32.MessageBoxW(None, "Congratulation, work is over!", "Pomodoro session", 0)        


pomodoro(0.01,0.05)
