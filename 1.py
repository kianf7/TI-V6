from microbit import *

pixel = [
    (2,2), (2,3), (2,3), (2,4), (1,3), (0,2), (1,2), (2,2), (1,0), (0,2), (0,3), (0,4), (1,3), (2,2), (3,2),
    (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)
]

def draw_house():
    index = 0
    paused = False
    
    while True:
        # (e) & (g) Button B: Reset / Button A: Pause & Fortsetzen
        if button_b.was_pressed():
            index = 0
            display.clear()
        
        if button_a.was_pressed():
            paused = not paused
            if paused:
                display.show("a")
            else:
                # (g) Bild wiederherstellen beim Fortsetzen
                display.clear()
                for i in range(index):
                    px, py = pixel[i]
                    display.set_pixel(px, py, 9)

        if not paused:
            if index < len(pixel):
                x, y = pixel[index]
                
                # (c) LED blinkt einmal kurz auf, bevor sie stabil bleibt
                display.set_pixel(x, y, 9)
                sleep(150)
                display.set_pixel(x, y, 0)
                sleep(150)
                display.set_pixel(x, y, 9)
                
                index += 1
                # (b) Geschwindigkeit: ca. 3 LEDs pro Sekunde (300ms + Pause)
                sleep(100) 
            else:
                # (d) Wenn Ende erreicht, von vorne beginnen
                sleep(1000)
                index = 0
                display.clear()
        
        sleep(50)
draw_house()


    