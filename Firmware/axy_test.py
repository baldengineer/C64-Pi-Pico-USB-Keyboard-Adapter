import board
import busio
import digitalio
import gc
from time import sleep
from sys import exit

ax_list = [
    {
        "name" : "ax0",
        "pin"  : board.GP13,
    },
    {
        "name" : "ax1",
        "pin"  : board.GP10,
    },
    {
        "name" : "ax2",
        "pin"  : board.GP9,
    },
    {
        "name" : "ax3",
        "pin"  : board.GP14,
    },
    {
        "name" : "ay0",
        "pin"  : board.GP11,
    },
    {
        "name" : "ay1",
        "pin"  : board.GP12,
    },
    {
        "name" : "ay2",
        "pin"  : board.GP19,
    },
]

on_sleep = 1
off_sleep = 1

for pin in ax_list:
    print(pin["name"])
    pin["pin"] = digitalio.DigitalInOut(pin["pin"])
    pin["pin"].direction = digitalio.Direction.OUTPUT
    pin["pin"].value = True
    sleep(on_sleep)
    pin["pin"].value = False
    sleep(off_sleep)
    pin["pin"].direction = digitalio.Direction.INPUT
