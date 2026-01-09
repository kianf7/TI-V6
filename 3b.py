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

#Pin Layouts
ROW_1 = const(21)
COL_1 = const(28)

ROW_2 = const(22)
COL_2 = const(11)

ROW_3 = const(15)
COL_3 = const(31)



#mem32[REG_GPIO_DIRSET] = 1 << ROW_2
#mem32[REG_GPIO_DIRSET] = 1 << COL_2



def set_row_high(const):
    mem32[REG_GPIO_OUTSET] = 1 << const

def set_row_low(const):
    mem32[REG_GPIO_OUTCLR] = 1 << const

def set_col_high(const):
    mem32[REG_GPIO_OUTSET] = 1 << const

def set_col_low(const):
    mem32[REG_GPIO_OUTCLR] = 1 << const

def set_led1():
    mem32[REG_GPIO_DIRSET] = 1 << ROW_1
    mem32[REG_GPIO_DIRSET] = 1 << COL_1
    set_row_high(ROW_1)
    set_col_low(COL_1)

def clr_led1():
    mem32[REG_GPIO_DIRCLR] = 1 << ROW_1
    mem32[REG_GPIO_DIRCLR] = 1 << COL_1
        

def set_led2():
    mem32[REG_GPIO_DIRSET] = 1 << ROW_2
    mem32[REG_GPIO_DIRSET] = 1 << COL_2
    set_row_high(ROW_2)
    set_col_low(COL_2)

def clr_led2():
    mem32[REG_GPIO_DIRCLR] = 1 << ROW_2
    mem32[REG_GPIO_DIRCLR] = 1 << COL_2

def set_led3():
    mem32[REG_GPIO_DIRSET] = 1 << ROW_3
    mem32[REG_GPIO_DIRSET] = 1 << COL_3
    set_row_high(ROW_3)
    set_col_low(COL_3)

def clr_led3():
    mem32[REG_GPIO_DIRCLR] = 1 << ROW_3
    mem32[REG_GPIO_DIRCLR] = 1 << COL_3

def pwm(percent, period):
   if percent <= 0:
       clr_led1()
       sleep(period)
       return
   time_on  = (percent/100) * period
   time_off = period - time_on
   set_led3()
   sleep(time_on)
   clr_led3()
   sleep(time_off)

timer = 0
brightness = 100
flag = False


while True:
    pwm(brightness, 20)
    timer += 1
    if timer % 10 == 0:
        if brightness <= 0 or brightness > 100:
            flag = not(flag)
        if flag:
            brightness += 10
        else:
            brightness -= 10
            
