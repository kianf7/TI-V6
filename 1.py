from microbit import *

pixel = [
    (2,2), (2,3), (2,4), (1,3), (0,2), (1,2), (2,2), (2,1), (1,0), (0,1),(0,2), (0,3), (0,4), (1,3), (2,2), (3,2),
    (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)
]

paused = False
global index
index = 0
reset = False
display_a = False
restore = False




    

@run_every(ms=10)
def check_buttons():
    global paused, index, reset, display_a, restore
    if button_a.was_pressed():
        paused = not paused
        if paused:
            display_a = True
        else:
            restore = True
    if button_b.was_pressed() and not(paused):
        index = 0
        reset = True
            
    
        

while True:
    if display_a:
        display.show("a")
        display_a = False
    if restore:
        display.clear()
        for i in range(index):
            px, py = pixel[i]
            display.set_pixel(px,py,9)
        restore = False
    if not paused:
        if reset:
            index = 0
            display.clear()
            reset = False
        if index < len(pixel):
            x, y = pixel[index]
    
            if display.get_pixel(x,y) == 9:
                display.set_pixel(x, y, 0)
                sleep(150)
                display.set_pixel(x, y, 9)
                sleep(150)
                display.set_pixel(x, y, 0)
                sleep(150)
                display.set_pixel(x,y,9)
            else:
                display.set_pixel(x, y, 9)
                sleep(150)
                display.set_pixel(x, y, 0)
                sleep(150)
                display.set_pixel(x, y, 9)
                
            index += 1
            sleep(100)
        else:
            sleep(1000)
            index = 0
            display.clear()


    
