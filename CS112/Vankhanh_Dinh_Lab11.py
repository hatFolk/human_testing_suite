def main():
	world = dict({(5,2):"store",(5,5):"dungeon 1", (1,7):"graveyard",
		(10,9):"riverdock", (8,3):"dungeon 2"})
	coord = (5,2)
	choice = 0
	while choice != "4":
		choice = input("""1. show my current location
2. what's here?
3. teleport
4. quit
> """)
		if choice == "1":
			where(coord)	
		if choice == "2":
			whats_here(world, coord)
		if choice == "3":
			coord = teleport(coord)

def where(coord):
	print("You are at {}.".format(coord))

def whats_here(world, coord):
	if coord in world:
		print("You can see: {}".format(world[coord]))
	else:
		print("Nothing.")

def teleport(coord):
	x = int(input("x to teleport to > "))
	y = int(input("y to teleport to > "))
	if (x not in range(11)) or (y not in range(11)):
		print("Off the map. Staying put.")
	else:
		coord = (x, y)
	return coord
main()
