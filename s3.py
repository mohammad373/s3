# s3
# /wp-contenr/plugins/
# 
import json
import os
import requests
import time
import sys
from colorama import Fore

def __1__():
    os.system("clear")
    print(Fore.YELLOW + "Hello . Welcome Back ;) ")
    target = input(Fore.BLUE + "\nEnter Your Address Target ==>  ")
    if target == "" or None :
        try:
            time.sleep(2)
            os.system("clear")
            print(Fore.RED + "Ok Good Lunch ;)")
        except:
            pass
    r = requests.get("http://" + target + "/wp-content/plugins/")
    if r.status_code == 404 or r.status_code == 500:
        try:
            print(Fore.YELLOW + "\n[!] - Your Target Is Not WordPress ;)")
            time.sleep(2)
            sys.exit()
        except:
            pass
    else:
        try:
            print(Fore.GREEN + "\n[+] - Your Target Is WordPress ;)")
            time.sleep(2)
            print(Fore.YELLOW + "\n[!] - This Is Checking The Your Target ...")
            time.sleep(2)
            print(Fore.YELLOW + "\n[!] - Pleass 3 sec Latter ...")
            time.sleep(3)
        except:
            pass
    j = requests.get("http://" + target + "/wp-json-wp/users/").text
    print(j)
__1__()
