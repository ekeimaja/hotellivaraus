

class Room():

	def __init__(self, header, amount, persons, text, petsAllowed):
		self.header = header
		self.amount = amount
		self.persons = persons
		self.text = text
		self.petsAllowed = petsAllowed

	def show_info(self):
		print(self.header, "\n" + "Huoneita yhteensä:", self.amount, "\n" + "Monenko hengen huone:", self.persons, "\n" + "Huoneen esittelyteksti:", self.text, "\n" + "Lemmikit sallittu:", self.petsAllowed)

	def reserve_room(room):
		if room.amount > 1:
			room.amount = room.amount - 1
			print("Huoneita vapaana:", room.amount)
		else:
			print("Ei", room.persons, "hengen huoneita vapaana!")