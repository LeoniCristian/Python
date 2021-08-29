import keyboard

stop = False
def onkeypress(event):
    global stop
    print(event.name)
    if event.name == 'esc':
        stop=True

keyboard.on_press(onkeypress)

while not stop:
    pass