from microbit import *


hausnikolaus = [(1,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4),
               (1,3), (0,2), (1,2), (2,2), (2,3), (2,4), (3,4),
               (4,4), (3,2), (2,2), (2,1), (1,0)]

def blink_led(x,y):
    display.set_pixel(x,y,9)
    sleep(100)
    display.set_pixel(x,y,0)
    sleep(100)
    display.set_pixel(x,y,9)

def paint_house():
    for i in hausnikolaus:
        if button_b.is_pressed():
            display.clear()
            break
        (x,y) = i
        blink_led(x,y)
    display.clear()
    sleep(1000)

while True:
    paint_house()


    
