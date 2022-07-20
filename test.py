# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @AbirHasan2005
#   and used by @rt-2
# Telegram Group: http://t.me/linux_repo
# Please give me credits if you use any codes from here.


#
#   Init(s)
#
import os, sys

#
#   Installs(s)
#
print("Initialyzing ...")
# ...
print("Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
os.system('pip3 install colorama')
os.system('pip3 install python-socks')
os.system('pip3 install async-timeout')

#
#   Import(s)
#
#import python-socks
import socket
import configparser
import colorama
import csv
import time
from telethon import TelegramClient
#from telethon.tl.functions.messages import GetDialogsRequest
#from telethon.tl.types import InputPeerEmpty


#
#   Var(s)
#
# ...
last_date = None
chunk_size = 200
groups=[]
# Color(s)
#Fix for windows
re=""
gr=""
cy=""
#Old Linux Colors
# re="\033[1;31m"
# gr="\033[1;32m"
# cy="\033[1;36m"

#
#   Functions
#
# Show Banner
def banner():
    # Clear terminal
	os.system('cls')
    # App name
	print(f"""            
        ____              _     ___          ______     __     ____        __ 
       / __ \____ __   __(_)___/ ( )_____   /_  __/__  / /__  / __ )____  / /_
      / / / / __ `/ | / / / __  /|// ___/    / / / _ \/ / _ \/ __  / __ \/ __/
     / /_/ / /_/ /| |/ / / /_/ /  (__  )    / / /  __/ /  __/ /_/ / /_/ / /_  
    /_____/\__,_/ |___/_/\__,_/  /____/    /_/  \___/_/\___/_____/\____/\__/  
                                                                            """)
    # Credits
	print(f"""         _                     _       ____  
        | |__  _   _      _ __| |_    |___ \ 
        | '_ \| | | |    | '__| __|____ __) |
        | |_) | |_| |    | |  | ||_____/ __/ 
        |_.__/ \__, |    |_|   \__|   |_____|
               |___/                      
               
               
	""")
    
# Exit Program
def exitProgram():
    print("\nExiting program ...\n\n")
    sys.exit(1)

# Send Error
def exitProgramWithError(message):
    os.system('clear')
    banner()
    print("\n\nERROR:")
    print(message)
    exitProgram()

#
#   Main
#
# Init(s)
colorama.init()
# ...
banner()
# ...
print("Initialyzed.")
# ...
#os.system("notepad config.data") # no need for that in windows

# # ...
# cpass = configparser.RawConfigParser()
# cpass.add_section('cred')
# xid = input(gr+"[+] Enter API ID : "+re)
# cpass.set('cred', 'id', xid)
# xhash = input(gr+"[+] Enter Hash : "+re)
# cpass.set('cred', 'hash', xhash)
# xphone = input(gr+"[+] Enter Phone Number: "+re)
# cpass.set('cred', 'phone', xphone)
# # ...
# with open('config.data', 'w') as setup:
	# cpass.write(setup)
    
# print(gr+"[+] Setup complete!")
# print(gr+"[+] Now you can run any tool!")
# print(gr+"[+] Make sure to read README.md before using this tool.")
# print(gr+"[+] https://github.com/AbirHasan2005/TelegramScraper/blob/master/README.md")
# print("\033[92m[+] Telegram Group: \033[96mhttp://t.me/linux_repo\033[0m")


# ...
#print("Hello world! (1)")


# Parsing config file
print(" Parsing config file ...")
cpass = configparser.RawConfigParser()
cpass.read('config.data')

# Storing config var(s)
try:
    # ...
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    name = "testName"

    print("ID:" + api_id)
    print("api_hash:" + api_hash)
    print("phone:" + phone)
    print("name:" + name)

    #client = TelegramClient('anon', api_id, api_hash)
    #client = TelegramClient('anon', api_id, api_hash, proxy=("socks5", '127.0.0.1', 4444))
except Exception :
    exitProgramWithError("File 'config.data' not formatted correctly.")

# Connecting
try:
    # ...
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
except Exception :
    exitProgramWithError("Cannot connect to Telegram API.")

# ...
# with TelegramClient('anon', api_id, api_hash) as client:
    # result = client(functions.messages.AddChatUserRequest(
        # chat_id=chatid,
        # user_id='username',
        # fwd_limit=42
    # ))
    # print(result.stringify())

# ...
print("Hello world! (2)")

# ...
# result = client(GetDialogsRequest(
             # offset_date=last_date,
             # offset_id=0,
             # offset_peer=InputPeerEmpty(),
             # limit=chunk_size,
             # hash = 0
         # ))
# chats.extend(result.chats)

# for chat in chats:
    # try:
        # if chat.megagroup== True:
            # groups.append(chat)
    # except:
        # continue
        
        
# ...
print("Hello world! (end)")