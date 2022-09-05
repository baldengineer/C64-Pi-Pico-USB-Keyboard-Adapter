# Blinky
import board
import busio
import digitalio
wirelesser_led = board.GP20
led = digitalio.DigitalInOut(wirelesser_led)
led.direction = digitalio.Direction.OUTPUT


# OLED Define
wirelesser_sda = board.GP16
wirelesser_scl = board.GP17

# UART Interface Define
wirelesser_tx = board.GP0
wirelesser_rx = board.GP1
uart = busio.UART(wirelesser_tx, wirelesser_rx, baudrate=115200)

# Mode select
wirelesser_hid = board.GP28
hid_enable = digitalio.DigitalInOut(wirelesser_hid)
hid_enable.direction = digitalio.Direction.INPUT
hid_enable.pull = digitalio.Pull.UP
wirelesser_serial = board.GP27
serial_enable = digitalio.DigitalInOut(wirelesser_serial)
serial_enable.direction = digitalio.Direction.INPUT
serial_enable.pull = digitalio.Pull.UP