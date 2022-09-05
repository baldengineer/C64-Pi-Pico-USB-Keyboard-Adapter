import board
import busio
import digitalio
import gc
from time import sleep
from sys import exit
import supervisor

# hide pinouts
import wirelesser
import mt88xx
import c64_keys

do_not_run = False

HIGH = True
LOW = False

def get_serial():
    value = 0
    while True:
        if supervisor.runtime.serial_bytes_available:
            value = input().strip()
            #print(f"Received: {value}\r")
            if value == "":
                continue
            return value


boot_mem = gc.mem_free()
print("MT8816 CP Demo Code Running with {} bytes free!!!".format(boot_mem))
wirelesser.led.value = True
sleep(1)
wirelesser.led.value = False
sleep(0.5)

if (do_not_run):
    print("You need to set do_not_run to false, duh.")
    exit()

mt88xx.ctl_245s(True) # Enables Them
mt88xx.init_values()
sleep(0.1)
# RESET goes LOW
mt88xx.reset.value = LOW
print("Doing the thing")

while(supervisor.runtime.serial_bytes_available):
    sleep(0.01)

while True:
    print("AX [0-15]> ",end='')
    ax = int(get_serial())
    print("AY [0-7]> ",end='')
    ay = int(get_serial())
    print("Shifted? [0/1]> ",end='')
    shifted = int(get_serial())
    # print("State [0/1]> ")
    # this_state = bool(int(get_serial))
    print(f"ax:[{ax}], ay:[{ay}], shifted:[{shifted}]")

    if (shifted==1):
        print("Shift On")
        mt88xx.set_data(1,7,True)
    mt88xx.set_data(ax,ay,True)
    sleep(0.1)
    mt88xx.set_data(ax,ay,False)
    if (shifted==1):
        print("Shift Off")
        mt88xx.set_data(1,7, False)
    #sleep(3)
    mt88xx.all_states(0)
    #sleep(1)   

while True:
    pass


# RESET goes high when done

# End stuff goes here, I guess
#mt88xx.ctl_245s(False) # Disables Them