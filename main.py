import room, rooms, sys, json, reservation

def load_texts():
	with open('text.json', 'r') as tekstitiedosto:
		return json.load(tekstitiedosto)

def jokujuttu():
	tekstit = load_texts()
	print(str(tekstit['aloitus']['logo']))
	print(str(tekstit['aloitus']['slogan']))
	print(str(tekstit['aloitus']['teksti']))

jokujuttu()

asd = input("> ")

if asd == "varaus":
	reservation.reservation()

if asd == "huoneet":
	print(room.Room.show_info(rooms.single_room))
	print()
	print(room.Room.show_info(rooms.dual_room))
	print()
	print(room.Room.show_info(rooms.quad_room))
	print()
	print(room.Room.show_info(rooms.pet_room))

if asd == "lisäpalvelut":
	tekstit = load_texts()
	print(str(tekstit['lisäpalvelut']))

if asd == "lisävarusteet":
	tekstit = load_texts()
	print(str(tekstit['lisävarusteet']))