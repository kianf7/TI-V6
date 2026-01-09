from microbit import *

while True:
    for i in range(0, 9):
        display.set_pixel(2, 2, i)
        sleep(100)
    
    for i in range(9, 0, -1):
        display.set_pixel(2, 2, i)
        sleep(100)
