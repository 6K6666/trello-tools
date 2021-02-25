import requests

json = requests.get("https://api.trello.com/1/boards/boardid/cards?key=apikey&token=token")

for card in json.json():
	sl = card['shortLink']
	req = requests.delete(f"https://api.trello.com/1/cards/{sl}?key=apikey&token=token")
	print(req)