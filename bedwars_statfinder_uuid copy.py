import requests


apikey = "your hypixel apikey"
uuid = input("player uuid: ")
url='https://api.hypixel.net/player?uuid='+str(uuid)
headers = {'API-Key':apikey}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

respone_dict = r.json()

print(f"name                 : {respone_dict['player']['playername']}")
print(f"bedwars games played : {respone_dict['player']['stats']['Bedwars']['games_played_bedwars']}")
print(f"bedwars wins         : {respone_dict['player']['stats']['Bedwars']['wins_bedwars']}")



