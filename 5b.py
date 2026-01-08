from microbit import *
import music
import time
import radio

command = [0,1,2,3,4]

notes = [
    'C4:4', 'E4:4', 'G4:4', 'C5:4',
    'G4:4', 'E4:4', 'C4:4', 'D4:4', 
    'F4:4', 'E4:4', 'D4:4', 'C4:4'
]

selection = 0
start = time.ticks_ms()
last_index = 0
radio.on()

def decode_message(message):
    try: 
        decoded = int(message)
        return decoded
    except: 
        return -1

def message_listener():
    message = radio.receive()
    if message:
        decoded = decode_message(message)
        if decoded in [0, 1, 2, 3, 4]:
            return decoded
        else:
            return -1

    return None


def show_temp():
    display.scroll(temperature())

def play_t1():
     music.pitch(262, 100)

def play_t2():
    music.pitch(349, 100) 


def play_song(selection, start):
    for note in notes:
        message = message_listener()
        if message is not None and message is not 3:
            if message == -1:
                display.show("X")
                sleep(1000)
                return 3, time.ticks_ms()
            selection = message
            return selection, time.ticks_ms()
            
        if button_a.was_pressed():
            music.stop()
            return 3, time.ticks_ms()
        music.play([note]) 
    return 3, start

def show_compass(selection, start):
    while True:
        display.scroll(compass.heading())
        message = message_listener()
        if message is not None and message is not 4:
            if message == -1:
                display.show("X")
                sleep(1000)
                return 4, time.ticks_ms()
            selection = message
            return selection, time.ticks_ms()
        if (button_a.was_pressed()):
            selection = 0
            return selection, time.ticks_ms()

while True:
    message= message_listener()

    if message is None: 
        send_Flag = False

    elif message == - 1: 
        start = time.ticks_ms()
        display.show("X")
        send_Flag = False
        sleep(1000)

    else:
        start = time.ticks_ms()
        selection = message
        send_Flag = True

    display.show(selection)
    if time.ticks_diff(time.ticks_ms(), start) >= 10000:
        selection, start = show_compass(selection, start)
    if button_a.was_pressed():
        selection = command[(selection + 1)%len(command)]
        start = time.ticks_ms()
    if button_b.was_pressed() or send_Flag:
        start = time.ticks_ms()
        if selection == 0:
            show_temp()
        elif selection == 1:
            play_t1()
        elif selection == 2:
            play_t2()
        elif selection == 3:
            selection, start = play_song(selection, start)
        elif selection == 4:
            selection, start = show_compass(selection, start)
        send_Flag = False
