from microbit import *
import music
import time
import radio
import log



notes = [
    'C4:4', 'E4:4', 'G4:4', 'C5:4',
    'G4:4', 'E4:4', 'C4:4', 'D4:4', 
    'F4:4', 'E4:4', 'D4:4', 'C4:4'
]

selection = 0
time_out = False
start = time.ticks_ms()
compass.calibrate()


def show_temp():
    temp = temperature()
    display.scroll(temp)

def play_t1():
     music.pitch(262, 100)

def play_t2():
    music.pitch(349, 100) 



def play_song():
    music.play(notes, wait=False)
    return selection, start


def show_compass():
    while True:
        display.scroll(compass.heading())
        if (button_a.was_pressed()):
            selection = 0
            return selection, time.ticks_ms(), True

while True:

    display.show(selection)
    if time.ticks_diff(time.ticks_ms(), start) >= 10000:
        selection = 5
        time_out = True
        
    if button_a.was_pressed():
        selection = (selection + 1)%6
        start = time.ticks_ms()
        
    if button_b.was_pressed() or time_out:
        start = time.ticks_ms()
        if selection == 0:
            show_temp()
        elif selection == 1:
            play_t1()
        elif selection == 2:
            play_t2()
        elif selection == 3:
            play_song()
        elif selection == 4:
            music.stop()
        elif selection == 5:
            selection, start, button_pressed = show_compass()
            
    time_out = False
