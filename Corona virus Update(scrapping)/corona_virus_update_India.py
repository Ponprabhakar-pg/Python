import requests
from bs4 import BeautifulSoup
from plyer import notification
import time


def notifyme(message):
    notification.notify(message=message,timeout=3)

while True:
    res=requests.get('https://www.worldometers.info/coronavirus/country/india/').text
    soup=BeautifulSoup(res,'html.parser')
    print(len(soup))
    soup.encode('utf-8')
    cases=soup.find("title").get_text().strip()
    notifyme(cases)
    time.sleep(10)
