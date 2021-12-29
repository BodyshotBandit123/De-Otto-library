import requests
import time
import datetime

apikey = "you hypixel apikey"
name = input("player name: ") 
print()
r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
url = "https://api.hypixel.net/skyblock/auction?player=" + str(r.json()["id"])
headers = {'API-Key':apikey}
r = requests.get(url, headers=headers)
respone_dict = r.json()
i = -1

for auction in respone_dict['auctions']:
    i+=1
    print(f"({i}) {auction['item_name']}\n")

itemnr = input("item number: ")
itemfinder = respone_dict['auctions'][int(itemnr)]
end = int(f"{itemfinder['end']}")
ts_epoch = end/1000.0
ts = datetime.datetime.fromtimestamp(ts_epoch).strftime('%d %H:%M:%S')
print(f"item name               : {itemfinder['item_name']}")
print(f"is the auction finished : {itemfinder['claimed']}")
print(f"highest bid amount      : {itemfinder['highest_bid_amount']}")
print(f"starting bid            : {itemfinder['starting_bid']}")
print(f"auction ends at         : {ts}")