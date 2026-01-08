from microbit import *


while True:
    for i in range(9, 0, -1):
        display.set_pixel(3,3,i)
        sleep(100)
