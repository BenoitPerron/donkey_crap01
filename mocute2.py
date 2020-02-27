from evdev import InputDevice, categorize, ecodes

moc = InputDevice('/dev/input/event5')

print(moc)

for event in moc.read_loop():
	if event.type == ecodes.EV_KEY:
		print(event)
#	print(categorize(event))

