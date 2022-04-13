import json
from room import *

def load_texts():
	with open('text.json', 'r') as tekstitiedosto:
		return json.load(tekstitiedosto)

tekstit = load_texts()

single_room = Room("Yhden hengen huone", 10, 1, tekstit['huoneet']['single'], "Ei")
dual_room = Room("Kahden hengen huone", 30, 2, tekstit['huoneet']['dual'], "Ei")
quad_room = Room("Neljän hengen huone", 15, 4, tekstit['huoneet']['quad'], "Ei")
pet_room = Room("Lemmikkihuone",15, 4, tekstit['huoneet']['pet'], "Kyllä")