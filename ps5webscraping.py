
import requests
from bs4 import BeautifulSoup
from requests.models import Response
from time import sleep
import random
from datetime import datetime


#URL = "https://www.amazon.nl/Sony-PS5-Standard-825GB-Europa/dp/B08LLZ2CWD"
URL = "https://www.amazon.nl/Sony-Playstation-Dualsense-Controller-Midnight/dp/B094YVTWF8/ref=sr_1_6"
TIJD= 4
prijsF = float(0)

while True:
    #we voegen een random getal toe om niet als een robot gedetecteerd te worden
    now = datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    oudeprijs = prijsF
    willekeurig = random.random()
    headers = {'User-Agent': f'Chrome/95.0.4638.69 (Windows NT 10.0;Win64; x64){willekeurig}'} 
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("span", {"class": "apexPriceToPay"})
    if results:
        prijs = results.find("span", {"class": "a-offscreen"})
        prijsS = prijs.string.replace("€", "").replace(",", ".")
        prijsF = float(prijsS)
        print(f"prijs: € {prijsF:.2f}")
        if oudeprijs < prijsF:
            print("Hij is duurder geworden")
        elif oudeprijs > prijsF:
            print("Hij is goedkoper geworden")
        else:
            print("De prijs is hetzelfde gebleven")
        print(f"Hij is beschikbaar\n")
    else: 
        print(f"Hij is niet beschikbaar\n")
    sleep(TIJD)

