import board
import digitalio

# C64 specific
c64_restore = board.GP2
restore = digitalio.DigitalInOut(c64_restore)
restore.direction = digitalio.Direction.OUTPUT