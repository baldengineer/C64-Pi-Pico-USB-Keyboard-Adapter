import board
import digitalio

# C64 specific
c64_restore = board.GP2
restore = digitalio.DigitalInOut(c64_restore)
restore.direction = digitalio.Direction.OUTPUT

key_map = {
	"0":(4,3,False),
	"1":(7,0,False),
	"2":(7,3,False),
	"3":(1,0,False),
	"4":(1,3,False),
	"5":(2,0,False),
	"6":(2,3,False),
	"7":(3,0,False),
	"8":(3,3,False),
	"9":(4,0,False),
	"-":(5,3,False),
	".":(5,4,False),
	":":(5,5,False),
	"@":(5,6,False),
	",":(5,7,False),
	
	"+":(5,0,False),
	#"":(6,0,False), # this is the GBP key
	"*":(6,1,False),
	";":(6,2,False),
	"=":(6,5,False),
	"/":(6,7,False),
	"<":(5,7,True),
	">":(5,4,True),
	"$":(1,3,True),
	"%":(2,0,True),
	"&":(2,3,True),
	"'":(3,0,True),
	"(":(3,3,True),
	")":(4,0,True),
	"[":(5,5,True),
	"]":(6,2,True),
	"?":(6,7,True),
	"!":(7,0,True),

	"a":(1,2,False),
	"b":(3,4,False),
	"c":(2,4,False),
	"d":(2,2,False),
	"e":(1,6,False),
	"f":(2,5,False),
	"g":(3,2,False),
	"h":(3,5,False),
	"i":(4,1,False),
	"j":(4,2,False),
	"k":(4,5,False),
	"l":(5,2,False),
	"m":(4,4,False),
	"n":(4,7,False),
	"o":(4,6,False),
	"p":(5,1,False),
	"q":(7,6,False),
	"r":(2,1,False),
	"s":(1,5,False),
	"t":(2,6,False),
	"u":(3,6,False),
	"v":(3,7,False),
	"w":(1,1,False),
	"x":(2,7,False),
	"y":(3,1,False),
	"z":(1,4,False),

	"\r":(0,1,False),
	" ":(7,4,False),



	"`":(7,1,False),     # left arrow character
	"~":(6,6,False),     # up arrow character (exp)

	 chr(27):(7,7,False), # run/stop
	 chr(34):(7,3,True),  # double quotes
	chr(127):(0,0,False), # backspace
}