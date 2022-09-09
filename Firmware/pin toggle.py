import board
import busio
import digitalio

pin = digitalio.DigitalInOut(board.GP13)
pin.direction = digitalio.Direction.OUTPUT

while True:
	pin.value = True
	pin.value = False