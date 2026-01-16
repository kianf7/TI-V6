from microbit import *
    
while True:
    display.set_pixel(0, 0, 9)  
    display.set_pixel(1, 1, 0)   
    sleep(1000)
    
    display.set_pixel(0, 0, 0)   
    display.set_pixel(1, 1, 9)  
    sleep(1000)