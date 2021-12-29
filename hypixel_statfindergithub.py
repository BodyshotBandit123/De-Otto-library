import requests
from requests.models import ReadTimeoutError

apikey = "your own hypixel apikey"
name = input("player name: ")
r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
url='https://api.hypixel.net/player?uuid='+str(r.json()["id"])
headers = {'API-Key':apikey}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")


respone_dict = r.json()

print(f"name                   : {respone_dict['player']['playername']}")
if "games_played_bedwars" in respone_dict['player']['stats']['Bedwars']:
    bedwarswins = int(f"{respone_dict['player']['stats']['Bedwars']['wins_bedwars']}")
    bedwarsgp = int(f"{respone_dict['player']['stats']['Bedwars']['games_played_bedwars']}")
    bedwarskills = int(f"{respone_dict['player']['stats']['Bedwars']['kills_bedwars']}")
    bedwarsdeaths = int(f"{respone_dict['player']['stats']['Bedwars']['deaths_bedwars']}")
    finalkills = int(f"{respone_dict['player']['stats']['Bedwars']['final_kills_bedwars']}")
    finaldeaths = int(f"{respone_dict['player']['stats']['Bedwars']['final_deaths_bedwars']}")
    print(f"bedwars games played   : {bedwarsgp}")
    print(f"bedwars wins           : {bedwarswins}")
    print(f"bedwars kd             : {bedwarskills/bedwarsdeaths:.2f}")
    print(f"bedwars final kill kd  : {finalkills/finaldeaths:.2f}")
    print(f"bedwars win percentage : {bedwarswins/bedwarsgp*100:.2f}%")
else:
    print("this person has never played bedwars")

if "games_played_skywars" in respone_dict['player']['stats']['SkyWars']:
    skykills = int(f"{respone_dict['player']['stats']['SkyWars']['kills']}")
    skydeaths = int(f"{respone_dict['player']['stats']['SkyWars']['deaths']}")
    print(f"skywars kd             : {skykills/skydeaths:.2f}")
else:
    print("This person has never played skywars")