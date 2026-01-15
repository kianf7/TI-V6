from microbit import *
from micropython import const
from machine import mem32

display.off()
# Base address for the GPIO 0 peripheal
REG_GPIO_P0 = const(0x50000000)
# When a 32bit value is written to this address, each bit set to 1 sets the output pin high
REG_GPIO_OUTSET = const(REG_GPIO_P0 + 0x508)
# When a 32bit value is written to this address, each bit set to 1 sets the output pin low
REG_GPIO_OUTCLR = const(REG_GPIO_P0 + 0x50C)
# When a 32bit value is written to this address, each bit set to 1 sets the pin to output
REG_GPIO_DIRSET = const(REG_GPIO_P0 + 0x518)
# When a 32bit value is written to this address, each bit set to 1 sets the pin to input
REG_GPIO_DIRCLR = const(REG_GPIO_P0 + 0x51C)


# Button A is pin 5 in the edge connector -> P0_14 in the nRF52833
ROW_1 = const(21)
COL_1 = const(28)

ROW_2 = const(22)
COL_2 = const(11)






def set_row_1_high():
    mem32[REG_GPIO_OUTSET] = 1 << ROW_1

def set_col_1_high():
    mem32[REG_GPIO_OUTSET] = 1 << COL_1

def set_row_1_low():
    mem32[REG_GPIO_OUTCLR] = 1 << ROW_1

def set_col_1_low():
    mem32[REG_GPIO_OUTCLR] = 1 << COL_1


def set_col_2_high():
    mem32[REG_GPIO_OUTSET] = 1 << COL_2

def set_row_2_high():
    mem32[REG_GPIO_OUTSET] = 1 << ROW_2

def set_col_2_low():
    mem32[REG_GPIO_OUTCLR] = 1 << COL_2

def set_row_2_low():
    mem32[REG_GPIO_OUTCLR] = 1 << ROW_2


def set_led1():
    mem32[REG_GPIO_DIRCLR] = 1 << ROW_2
    mem32[REG_GPIO_DIRCLR] = 1 << COL_2
    mem32[REG_GPIO_DIRSET] = 1 << ROW_1
    mem32[REG_GPIO_DIRSET] = 1 << COL_1
    set_row_1_high()
    set_col_1_low()
        

def set_led2():
    mem32[REG_GPIO_DIRCLR] = 1 << ROW_1
    mem32[REG_GPIO_DIRCLR] = 1 << COL_1
    mem32[REG_GPIO_DIRSET] = 1 << ROW_2
    mem32[REG_GPIO_DIRSET] = 1 << COL_2
    set_row_2_high()
    set_col_2_low()

while True:
    set_led1() 
    sleep(1000)
    set_led2()
    sleep(1000)
