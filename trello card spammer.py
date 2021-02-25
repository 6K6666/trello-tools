import requests

key = 'trello API key'
token = 'trello token'

lists = requests.get(f"https://api.trello.com/1/boards/boardid/lists?key={key}&token={token}") ## replace boardid with the board id that you will spam cards in

for lis in lists.json():
	for x in range(1000):
		lid = lis['id']
		req = requests.post(f"https://api.trello.com/1/cards?key={key}&token={token}&idList={lid}&name=nuked%nuked?%20nuked%20nuked%0nuked%0nuked")
		print(req)