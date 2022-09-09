import board
import busio
import digitalio
import gc
from time import sleep
from sys import exit
import supervisor
import usb_cdc

# hide pinouts
import wirelesser
import mt88xx
import c64_keys

do_not_run = False

HIGH = True
LOW = False

#Serial Port Stuff
serial = usb_cdc.data
serial_connect_flag = True
serial.timeout = 0 # don't wait


def handle_serial():
    global serial_connect_flag
    if (serial.connected):
        if (serial_connect_flag):
            print("Connected!")
            serial_connect_flag = False
        if (serial.in_waiting > 0):
            byte = serial.read(1).decode('utf-8')
            set_key(byte, False, False, False)
            #print(byte.decode('utf-8'),end='')

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
#print("####\n# YOU DISABLED THE CHIP!!!!\n# There are three returns!\n####")
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

def set_colrow(ax,ay,shifted):
    if (shifted==1):
        mt88xx.set_data(1,7,True)
    mt88xx.set_data(ax,ay,True)
    sleep(0.1)
    mt88xx.set_data(ax,ay,False)
    if (shifted==1):
        mt88xx.set_data(1,7, False)
    return

    # key_map = [
    # {
    #     "char":"a"
    #     "row" : 1
    #     "col" : 2
    # },

def set_key(key,shifted,ctrled,cbmkey):
    #print(key,end='')
    ax = 0
    ay = 0
    decoded = False
    try:
        coords = c64_keys.key_map[key]
        ax,ay = coords
        decoded = True
    except:
        print(f"Don't know: [{key}]")

    if (decoded):
        print(f"key: {key}, ax: {ax}, ay: {ay}")
        set_colrow(ax,ay,False)
    return

while True:
    handle_serial()


    #sleep(3)
    #mt88xx.all_states(0)
    #sleep(1)   

while True:
    pass

# End stuff goes here, I guess
#mt88xx.ctl_245s(False) # Disables Them



    # print("AX [0-15]> ",end='')
    # ax = int(get_serial())
    # print("AY [0-7]> ",end='')
    # ay = int(get_serial())
    # print("Shifted? [0/1]> ",end='')
    # shifted = int(get_serial())
    # # print("State [0/1]> ")
    # # this_state = bool(int(get_serial))
    # print(f"ax:[{ax}], ay:[{ay}], shifted:[{shifted}]")