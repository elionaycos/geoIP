import requests
from bs4 import BeautifulSoup
from sys import argv
import re


class GeoIP:
    def __init__(self, ip):
        self.ip = ip
        self.host = "https://www.geolocation.com/?ip={}".format(ip)
        
        self.browser = requests.get(self.host)

    def getData(self):
        self.content = bytes(self.browser.content).decode("UTF-8")
        self.className = '_class="table table-ip table-striped"'
        self.soup = BeautifulSoup(self.content, "html.parser")
        self.data_ip = self.soup.find(
            "table", {"class": "table table-ip table-striped"})
        lat = ""
        lon = ""
        for item in self.data_ip.find_all("td"):
            item = (re.sub(r'[\n\t]','',item.text)).replace("\r",": ")
            
            
            
            if item and item != "W3C Geolocation API Demo":
                item = str(item[0:len(item)-2])
                if "Latitude" in item:
                    lat = item.split(": ")[1]
                elif  "Longitude" in item:
                    lon = item.split(": ")[1]
                    
                
                print("\033[92m [x] {} < \033[00m".format(item))
        self.map_host = "https://www.google.com/maps?q={},{}".format(lat,lon)
        print("\n\r")
        print("\033[93m [ok] IP: {} < \033[00m".format(self.ip))
        print("\033[94m [ok] Google Map: {} < \033[00m".format(self.map_host))


ip = "170.231.133.46"

geoIP = GeoIP(ip)
geoIP.getData()
