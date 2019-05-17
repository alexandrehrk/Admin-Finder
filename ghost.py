# coding: utf-8

# Twitter: @KryptonWave1
# Discord: KriotonWave#9010

# HYS TEAM

import argparse
import sys
import os


# Limpar tela
os.system("cls||clear")

index = (r"""
   ________               __  _______           __         
  / ____/ /_  ____  _____/ /_/ ____(_)___  ____/ /__  _____
 / / __/ __ \/ __ \/ ___/ __/ /_  / / __ \/ __  / _ \/ ___/
/ /_/ / / / / /_/ (__  ) /_/ __/ / / / / / /_/ /  __/ /    
\____/_/ /_/\____/____/\__/_/   /_/_/ /_/\__,_/\___/_/     
""")

try:
    import requests
    from colorama import Fore as F
    from colorama import *

except:
      print (index)
      print ("[!] Please Install Requests: pip install requests")
      print ("[!] Please Install Colorama: pip install colorama")
      exit()

print (Style.BRIGHT + F.WHITE + index + Style.RESET_ALL + F.RESET)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

parser = argparse.ArgumentParser(description='Comandos de como usar: ')
parser.add_argument("--url", type=str, metavar="target", required=False , help="Target WebSite!")
parser.add_argument("--list", type=str, metavar="wordlist" , required=False , help="Wordlist.txt")
args = parser.parse_args()

try:
    with open(args.list,'r') as word:
         brute = word.readlines()

         for wordlist in brute:
             x = args.url
             y = (x + wordlist).rstrip('\n')
             req = requests.get(y, headers=headers)
             if req.status_code == 200:
                 print (Style.BRIGHT + F.WHITE + "[+] Encontrada: " + F.RESET + F.GREEN + y + F.RESET + Style.RESET_ALL)
             else:
                  if req.status_code != 200:
                     print (Style.BRIGHT + F.RED + "[-] Fail: " + y + F.RESET + Style.RESET_ALL)

except:
       print (Style.BRIGHT + F.GREEN + "Usage: " + sys.argv[0] + " --help" + F.RESET + Style.RESET_ALL)

#

