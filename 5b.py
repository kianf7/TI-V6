from microbit import *
import music
import time
import radio
import log

command = [0,1,2,3,4,5]

notes = [
    'C4:4', 'E4:4', 'G4:4', 'C5:4',
    'G4:4', 'E4:4', 'C4:4', 'D4:4', 
    'F4:4', 'E4:4', 'D4:4', 'C4:4'
]

selection = 0
time_out = False
start = time.ticks_ms()
last_index = 0
radio.on()
radio.config(group=60)
global send_Flag
send_Flag = False
compass.calibrate()

def log_message(message):
    timestamp = time.ticks_ms()
    temp = temperature()
    volume = microphone.sound_level()
    light = display.read_light_level()

    log.add({
        'group_id': 60,
        'message': message,
        'temperature': temp,
        'volume': volume,
        'lightlevel': light,
        'timestamp': timestamp
    })
    

def decode_message(message):
    try: 
        decoded = int(message)
        return decoded
    except: 
        return -1

def message_listener():
    message = radio.receive()
    if message:
        log_message(message)
        decoded = decode_message(message)
        if decoded in [0, 1, 2, 3, 4, 5]:
            return decoded
        else:
            return -1
    return None

def show_temp():
    temp = temperature()
    display.scroll(temp)
    radio.send(str(temp))

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
        if message is not None and message is not 5:
            if message == -1:
                display.show("X")
                sleep(1000)
                return 5, time.ticks_ms(), False
            selection = message
            return selection, time.ticks_ms(), False
        if (button_a.was_pressed()):
            selection = 0
            return selection, time.ticks_ms(), True

while True:
    message= message_listener()

    if message is None: 
        pass

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
        selection = 5
        time_out = True
    if button_a.was_pressed():
        selection = command[(selection + 1)%len(command)]
        start = time.ticks_ms()

    if button_b.was_pressed() or send_Flag or time_out:
        start = time.ticks_ms()
        if selection == 0:
            show_temp()
            send_Flag = False
        elif selection == 1:
            play_t1()
            send_Flag = False
        elif selection == 2:
            play_t2()
            send_Flag = False
        elif selection == 3:
            selection, start = play_song(selection, start)
            if selection == 3:
                send_Flag = False
            else:
                send_Flag = True
        elif selection == 4:
            music.stop()
            display.show("S")
            sleep(500)
            send_Flag = False
        elif selection == 5:
            selection, start, button_pressed = show_compass(selection, start)
            send_Flag = not(button_pressed)
    time_out = False
