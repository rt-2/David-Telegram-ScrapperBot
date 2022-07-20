# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @AbirHasan2005
#   and used by @rt-2
# Telegram Group: http://t.me/linux_repo
# Please give me credits if you use any codes from here.



#
#   Functions
#
# Show Banner
def clsAndShowBanner():
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
	print(f"""             _                     _       ____  
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
    #clsAndShowBanner()
    print("\n\nERROR:")
    print(message)
    exitProgram()


#
#   Init(s)
#
# ...
import os, sys
# ...
clsAndShowBanner()

#
#   Installs(s)
#
print("Initialyzing ...")
# ...
print("Installing requierments ...")
# #os.system('python3 -m pip install telethon')
# os.system('pip3 install telethon')
# os.system('pip3 install python-socks')
# os.system('pip3 install async-timeout')
# os.system('pip3 install asyncio')

#
#   Import(s)
#
#import python-socks
import socket
import configparser
#import colorama
import csv
import time
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


#
#   Var(s)
#
# ...
api_id = None
api_hash = None
phone = None
name = None
last_date = None
chunk_size = 200
groups=[]
chats = []
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
#   Main
#
# Init(s)
#colorama.init()
# ...
clsAndShowBanner()
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

# Main/All?
async def main():

    # ...
    print("\nTESTING: 'main' starting ...\n")

    # ...
    print("TESTING: 'main' started.")


    # Parsing config file
    print(" Parsing config file ...")
    cpass = configparser.RawConfigParser()
    cpass.read('config.data')

    # Storing config var(s)
    try:
        # ...
        api_id = cpass['cred']['id']
        api_hash = cpass['cred']['hash']
        bot_token = cpass['cred']['bot_token']
        phone = cpass['cred']['phone']
        name = "testName"

        print("ID:" + api_id)
        print("api_hash:" + api_hash)
        print("bot_token:" + bot_token)
        print("phone:" + phone)
        print("name:" + name)

        #client = TelegramClient('anon', api_id, api_hash)
        #client = TelegramClient('anon', api_id, api_hash, proxy=("socks5", '127.0.0.1', 4444))
    except Exception :
        exitProgramWithError("File 'config.data' not formatted correctly.")


    # Connecting
    try:
        # ...

        # print("test1")
        # #client = TelegramClient(name, api_id, api_hash)
        # print("test2")
        # #await client.start()
        # print("test3")
        # bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
        # print("test4")
        client = TelegramClient(None, api_id, api_hash)
        client.session.set_dc(2, '149.154.167.40', 80)
        client.start(
            phone='9996621234', code_callback=lambda: '22222'
        )
            
        #client = TelegramClient(phone, api_id, api_hash)
        #client.connect()
    except Exception :
        exitProgramWithError("Cannot connect to Telegram API.")

    # Verifying auth
    if not client.is_user_authorized():
        #exitProgramWithError("Account not authorized.")
        client.send_code_request(phone)
        os.system('clear')
        banner()
        client.sign_in(phone, input(gr+'[+] Enter the verification code: '+yo))
        sys.exit(1)


    # async with TelegramClient(name, api_id, api_hash) as client:
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


    # with TelegramClient(name, api_id, api_hash) as client:
        # await print("INSIDE")
        
    # result = client(GetDialogsRequest(
                 # offset_date=last_date,
                 # offset_id=0,
                 # offset_peer=InputPeerEmpty(),
                 # limit=chunk_size,
                 # hash = 0
             # ))
    #chats.extend(result.chats)


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
    
    # ...
    print("\nTESTING: 'main' ending ...\n")
    
    
    
    
    
    
    
    
#
#   executing 'main'
#

asyncio.get_event_loop().run_until_complete(main())


#task = loop.create_task(main())
#loop.run_until_complete(task)
