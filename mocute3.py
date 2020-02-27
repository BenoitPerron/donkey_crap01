from evdev import InputDevice, categorize, ecodes

moc = InputDevice('/dev/input/event5')

print(moc)

for event in moc.read_loop():
	if event.type in [ ecodes.EV_KEY ] and event.code in [ ecodes.BTN_START, ecodes.BTN_WEST, ecodes.BTN_EAST, ecodes.BTN_NORTH, ecodes.BTN_SOUTH ]:
#		print('BTN: ', event)
		if event.value == 1:
			print('BTN: ', event)
	elif event.type in [ ecodes.EV_ABS ] and event.code in [ ecodes.ABS_X, ecodes.ABS_Y ]:
		print('ABS: ', event)


