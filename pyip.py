from columnar import columnar
import requests
import os
from art import *
import sys

def clear():
  if os.name == "nt":
    os.system("cls")
  elif os.name == "posix":
    os.system("clear")
  else:
    print(f"OS: {os.name} | Could not clear the console but will continue.\n")
    pass


clear()
print(text2art("PyIP") + "Made by github.com/iUseYahoo\nIf you want to track yourself just press enter.\n")

class mainClass:
    def trackIP(grabip):


        if grabip == "":
          print("[+] Tracking your own IP.")
        else:
          print(f"[*] Tracking IP: {grabip}\n")
          pass
          
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
      
        print(columnar(table_data, table_headers))

    def main():
        while True:
            grabip = input("Enter IP: ")

            if grabip == "clear":
                clear()
                print(text2art("PyIP") + "Made by github.com/iUseYahoo\nIf you want to track yourself just press enter.\n")
            elif grabip == "exit":
              sys.exit()
            else:
              mainClass.trackIP(grabip)
            
if __name__ == '__main__':
    mainClass.main()
