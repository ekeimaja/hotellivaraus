import room
import rooms

def reservation():

	allowed = False

	pets = input("Onko mukanasi lemmikkieläimiä? (k/e) ")

	guest_amount = input("Kuinka monta vierasta? ")

	if pets == 'e' or pets == 'E':
		while(guest_amount <= '4'):
			if guest_amount == '1':
				room.Room.reserve_room(rooms.single_room)
				allowed = True
			elif guest_amount == '2':
				room.Room.reserve_room(rooms.dual_room)
				allowed = True
			elif guest_amount >= '3':
				room.Room.reserve_room(rooms.quad_room)
				allowed = True
			break
	if pets == 'k' or pets == 'K':
		room.Room.reserve_room(rooms.pet_room)
		allowed = True


	if allowed:
		for i in range(eval(guest_amount)):
			guests = []
			guestName = input("Kirjoita vieraan " + str(i+1) + " koko nimi: ")
			guests.append(guestName)
	
		print("Olet tehnyt varauksen " + str(eval(guest_amount)) + " henkilölle. Varaus on tehty henkilö(i)lle: ", guests[:])
	else:
		print("Varauksen teossa tapahtui virheitä :(")