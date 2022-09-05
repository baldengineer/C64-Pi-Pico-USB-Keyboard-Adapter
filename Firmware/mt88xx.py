import board
import busio
import digitalio
from time import sleep

HIGH = True
LOW = False

# MT88xx Control Signals
mt88xx_ctl245_dir = board.GP7  #aka U3
mt88xx_ctl245_en  = board.GP3  #aka U3
mt88xx_mtx245_dir = board.GP18  #aka U2
mt88xx_mtx245_en  = board.GP8  #aka U2
mt88xx_strobe = board.GP6
mt88xx_data = board.GP5
mt88xx_cs = board.GP4
mt88xx_reset = board.GP15

strobe = digitalio.DigitalInOut(mt88xx_strobe)
strobe.direction = digitalio.Direction.OUTPUT

data = digitalio.DigitalInOut(mt88xx_data)
data.direction = digitalio.Direction.OUTPUT

cs = digitalio.DigitalInOut(mt88xx_cs)
cs.direction = digitalio.Direction.OUTPUT

reset = digitalio.DigitalInOut(mt88xx_reset)
reset.direction = digitalio.Direction.OUTPUT

ctl245_dir = digitalio.DigitalInOut(mt88xx_ctl245_dir)
ctl245_dir.direction = digitalio.Direction.OUTPUT

ctl245_en = digitalio.DigitalInOut(mt88xx_ctl245_en)
ctl245_en.direction = digitalio.Direction.OUTPUT

mtx245_dir = digitalio.DigitalInOut(mt88xx_mtx245_dir)
mtx245_dir.direction = digitalio.Direction.OUTPUT

mtx245_en = digitalio.DigitalInOut(mt88xx_mtx245_en)
mtx245_en.direction = digitalio.Direction.OUTPUT

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
for pin in ax_list:
	pin["pin"] = digitalio.DigitalInOut(pin["pin"])
	pin["pin"].direction = digitalio.Direction.OUTPUT

ax0 = 0
ax1 = 1
ax2 = 2
ax3 = 3

ay0 = 4
ay1 = 5
ay2 = 6

def decode_x(addrx):
	# Hey, guess what, read the data sheet
	# X coordiantes are not linear
	if (addrx == 6):
		addrx = 8
	if (addrx == 7):
		addrx = 9
	ax_list[ax0]["pin"].value = bool(addrx & 0x1)
	ax_list[ax1]["pin"].value = bool(addrx & 0x2)
	ax_list[ax2]["pin"].value = bool(addrx & 0x4)
	ax_list[ax3]["pin"].value = bool(addrx & 0x8)
	return

def decode_y(addry):
	ax_list[ay0]["pin"].value = bool(addry & 0x1)
	ax_list[ay1]["pin"].value = bool(addry & 0x2)
	ax_list[ay2]["pin"].value = bool(addry & 0x4)
	return

def set_data(addrx,addry,sw_data):
	# set address
	decode_x(addrx)
	decode_y(addry)
	# set data 
	data.value = int(sw_data)
	sleep(.001)

	# CS goes high
	cs.value = HIGH
	sleep(.0001)

	# strobe high for 20ns
	strobe.value = HIGH
	sleep(.0001)


	# stobe go low
	strobe.value = LOW
	sleep(.0001)
	# CS goes low
	cs.value = LOW
	return

def all_states(data):
	for col in range(0,8):
		for row in range(0,8):
			set_data(col,row,data)
	return

def init_values():
	# put mt88xx into known state
	print("Init MT8816 State")
	reset.value = True
	sleep(0.1)
	reset.value = False
	sleep(0.1)
	cs.value = True
	sleep(0.1)
	for pin in ax_list:
		pin["pin"].value = False
	sleep(0.1)
	data.value = False	
	sleep(0.1)
	strobe.value = False
	sleep(0.1)
	cs.value = False
	sleep(0.2)
	reset.value = True
	return

# def blink_axy():
# 	# put mt88xx into known state

# 	print ("starting...")
# 	while(True):
# 		for pin in ax_list:
# 			pin["pin"].value = True
# 		sleep(0.001)
# 		for pin in ax_list:
# 			pin["pin"].value = False
# 		sleep(0.001)
# 	print("done!")
# 	return


def ctl_245s(state):
	# state is human readable, CE is active low
	# U2
	mtx245_dir.value = True  # A to B
	mtx245_en.value = not state

	# U3
	ctl245_dir.value = False # B to A
	ctl245_en.value = not state
	return