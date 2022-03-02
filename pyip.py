from columnar import columnar
import requests
import os
from art import *

os.system('cls')
print(text2art("PyIP") + "Made by github.com/iUseYahoo\nIf you want to track yourself just press enter.\n")

class mainClass:
    def trackIP(grabip):
        showcont = requests.get(f"http://ip-api.com/json/{grabip}?fields=continent")
        showcoun = requests.get(f"http://ip-api.com/json/{grabip}?fields=country")
        showregi = requests.get(f"http://ip-api.com/json/{grabip}?fields=regionName")
        showcity = requests.get(f"http://ip-api.com/json/{grabip}?fields=city")
        showpost = requests.get(f"http://ip-api.com/json/{grabip}?fields=zip")
        showisp = requests.get(f"http://ip-api.com/json/{grabip}?fields=isp") 
        
        table_headers = ['Name', 'Information']
        table_data = [
            ["Continent ", showcont.text.strip('}{":')],
            ["Country ", showcoun.text.strip('}{":')],
            ["Region Name ", showregi.text.strip('}{":')],
            ["City ", showcity.text.strip('}{":')],
            ["Post Code (ZIP) ", showpost.text.strip('}{":')],
            ["Internet Provider (ISP) ", showisp.text.strip('}{":')]
        ]

        print(f"[*] Tracking IP: {grabip}\n")
        print(columnar(table_data, table_headers))

    def main():
        while True:
            grabip = input("Enter IP: ")

            if grabip == "clear":
                os.system('cls')
                print(text2art("PyIP") + "Made by github.com/iUseYahoo\nIf you want to track yourself just press enter.\n")

            else:
                mainClass.trackIP(grabip)
            
if __name__ == '__main__':
    mainClass.main()
