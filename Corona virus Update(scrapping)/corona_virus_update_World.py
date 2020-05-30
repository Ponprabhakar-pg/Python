import requests
from bs4 import BeautifulSoup
from plyer import notification
import time


def notifyme(title,message):
    notification.notify(title=title,message=message,timeout=3)

while True:
    res=requests.get('https://www.worldometers.info/coronavirus/').text
    soup=BeautifulSoup(res,'html.parser')
    soup.encode('utf-8')
    cases=soup.find("div",{"class":"maincounter-number"}).get_text().strip()
    recovered=soup.find("div",{"class":"maincounter-number","style":"color:#8ACA2B "}).get_text().strip()
    notifyme('World Wide \nTotal Number of Cases: ',cases)
    notifyme('World Wide \nTotal Number of Recovery: ',recovered)
    time.sleep(10)
