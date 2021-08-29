import keyboard
import time 
import random
import win32api, win32con
import os
import re   

TONE = {
    'REST'   : 0,
    'GbelowC' : 196,
    'A'      : 220,
    'Asharp' : 233,
    'B'      : 247,
    'C'      : 262,
    'Csharp' : 277,
    'D'      : 294,
    'Dsharp' : 311,
    'E'      : 330,
    'F'      : 349,
    'Fsharp' : 370,
    'G'      : 392,
    'Gsharp' : 415,
    'Asup'   : 437
    }

DEF_TIME = 1600

DURATION = {
    'WHOLE'     : DEF_TIME,
    'THREE_QUARTERS':DEF_TIME/3 * 2,
    'HALF'      : DEF_TIME/2,
    'THIRD'     : DEF_TIME/3,
    'QUARTER'   : DEF_TIME/4,
    'EIGHTH'    : DEF_TIME/8,
    'SIXTEENTH' : DEF_TIME/16,
    }

def default_beep(i,j): 
    win32api.Beep(int(i),int(j))
       
def beep(clock_freq=1,clock_time=1000,bp_freq=-1,bp_time=100):        
        t=0
        while t < clock_time:
            if(bp_freq<=0):               
                win32api.Beep(random.randint(1000,3200), int(bp_time))
            else:
                win32api.Beep(int(bp_freq), int(bp_time))            
                
            time.sleep(1/clock_freq)
            t += 1000/clock_freq
            #print(t,clock_time,1/clock_freq)

def play_song(song):
    for i in song:
        tone =TONE[i[0]]
        duration = DURATION[i[1]] if(len(i)>1) else 1600/4
        print(tone,duration)
        if(tone == 'REST'):
            time.sleep(duration)
        else:
            default_beep(tone,duration)

def play_song_raw(song):
    for i in song:
        tone,duration = i
        default_beep(tone,duration)

def load_song(song='Tetris'): 
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,f'Songs\{song}.txt')
    #play_song(song)
    with open(filename) as f:
        for i in f:
            data = re.sub('[\[\]\(\)]', '', i).split(',')
            it = iter(data)
            data = zip(it,it)
    return data
"""
TETRIS = [
    ('E',       'QUARTER'),#'SIXTEENTH'
    ('B',       'EIGHTH'),
    ('C',       'EIGHTH'),
    ('D',       'QUARTER'),
    ('C',       'EIGHTH'),
    ('B',       'EIGHTH'),
                
    ('A',       'QUARTER'),
    ('A',       'EIGHTH'),
    ('C',       'EIGHTH'),
    ('E',       'QUARTER'),
    ('D',       'EIGHTH'),
    ('C',       'EIGHTH'),
    
    ('B',       'QUARTER'),
    ('B',       'EIGHTH'),
    ('C',       'EIGHTH'),
    ('D',       'QUARTER'),
    ('E',       'QUARTER'),

    ('C',       'QUARTER'),
    ('A',       'QUARTER'),
    ('A',       'QUARTER'),
    ('REST',    'QUARTER'),

    ('REST',    'EIGHTH'),
    ('D',       'QUARTER'),
    ('F',       'EIGHTH'),
    ('Asup',       'QUARTER'),
    ('G',       'EIGHTH'),
    ('F',       'EIGHTH'),
    
    ('E',       'QUARTER'),
    ('E',       'EIGHTH'),
    ('C',       'EIGHTH'),
    ('E',       'QUARTER'),
    ('D',       'EIGHTH'),
    ('C',       'EIGHTH'),
    
    ('B',       'QUARTER'),
    ('B',       'EIGHTH'),
    ('C',       'EIGHTH'),
    ('D',       'QUARTER'),
    ('E',       'QUARTER'),

    ('C',       'QUARTER'),
    ('A',       'QUARTER'),
    ('A',       'QUARTER')
]

MARY = [
    ('B','QUARTER'),
    ('A',       'QUARTER'),
    ('GbelowC', 'QUARTER'),
    ('A',       'QUARTER'),
    ('B',       'QUARTER'),
    ('B',       'QUARTER'),
    ('B',       'HALF'),
    ('A',       'QUARTER'),
    ('A',       'QUARTER'),
    ('A',       'HALF'),
    ('B',       'QUARTER'),
    ('D',       'QUARTER'),
    ('D',       'HALF')
]

ZELDA = [
    ('C','QUARTER'),
    ('Csharp',       'QUARTER'),
    ('D', 'QUARTER'),
    ('E',       'QUARTER'),
    ('B',       'QUARTER'),
    ('B',       'QUARTER'),
    ('B',       'HALF'),
    ('A',       'QUARTER'),
    ('A',       'QUARTER'),
    ('A',       'HALF'),
    ('B',       'QUARTER'),
    ('D',       'QUARTER'),
    ('D',       'HALF')
]
"""    
ZELDA = [
    ('F','QUARTER'),
    ('Fsharp',       'QUARTER'),
    ('G', 'QUARTER'),
    ('REST','SIXTEENTH'),
    ('Gsharp',       'HALF')
    ]
if(__name__=='__main__'):
    #play_song_raw(load_song('TETRIS'))    
    play_song(ZELDA)