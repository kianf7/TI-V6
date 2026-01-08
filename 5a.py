from microbit import *
import music
import time

command = [0,1,2,3,4]

notes = [
    'C4:4', 'E4:4', 'G4:4', 'C5:4',  
    'G4:4', 'E4:4', 'C4:4', 'D4:4', 
    'F4:4', 'E4:4', 'D4:4', 'C4:4'  
]

selection = 0
start = time.ticks_ms()
last_index = 0


def show_temp():
    display.scroll(temperature())

def play_t1():
     music.pitch(262, 100)      

def play_t2():
    music.pitch(349, 100) 
    
    
def play_song(start):
    for note in notes:
        if button_a.was_pressed():
            music.stop()
            return time.ticks_ms()
        music.play([note]) 
    return start
        
def show_compass(selection, start):
    while True:
        display.scroll(compass.heading())
        if (button_a.was_pressed()):
            selection = command[(selection + 1)%len(command)]
            return selection, time.ticks_ms()
            
    



 
while True:
    display.show(selection)
    if time.ticks_diff(time.ticks_ms(), start) >= 10000:
        selection, start = show_compass(selection, start)
    if button_a.was_pressed():
        selection = command[(selection + 1)%len(command)]
        start = time.ticks_ms()
    if button_b.was_pressed():
        start = time.ticks_ms()
        if selection == 0:
            show_temp()
        elif selection == 1:
            play_t1()
        elif selection == 2:
            play_t2()
        elif selection == 3:
            start = play_song(start)
        elif selection == 4:
            selection, start = show_compass(selection, start)
