from microbit import *
import time

#MORSE CODE
# A kurz, B lang

morse_code = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", 
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", 
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", 
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", 
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", 
    "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3", 
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", 
    "----.": "9"}


last_event = time.ticks_ms()
userInput = ""

while True:
    if button_b.was_pressed():
        userInput += "-"
        display.show("-")
        last_event = time.ticks_ms()
        
    elif button_a.was_pressed():
        userInput += "."
        display.show("*")
        last_event = time.ticks_ms()
        
    if time.ticks_diff(time.ticks_ms(), last_event) > 1000 and len(userInput) > 0:
        result = morse_code.get(userInput, "?")
        display.show(result)
        sleep(1000)
        userInput = ""

        last_event = time.ticks_ms()
        display.clear()
        