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
TELEGRAM_TEST_IP = '149.154.167.40'
TELEGRAM_TEST_PORT = 80
ONLY_MEGA_GROUPS = False
api_id = None
api_hash = None
bot_token = None
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

# Main/All?

# Parsing config file
print(" Parsing config file ...")
cpass = configparser.RawConfigParser()
cpass.read('config.data')

# Storing config var(s)
try:
    # ...
    api_id = cpass['cred']['app_id']
    api_hash = cpass['cred']['hash']
    bot_token = api_id + ":" + api_hash
    phone = cpass['cred']['phone']
    name = "testName"

    print("\nConfigurations:")
    print("ID:" + api_id)
    print("api_hash:" + api_hash)
    print("bot_token:" + bot_token)
    print("phone:" + phone)
    print("name:" + name)
    print("\n")
    
except Exception :
    exitProgramWithError("File 'config.data' not formatted correctly.")

# Connecting
try:
    # ...        
    client = TelegramClient(name, api_id, api_hash)
except Exception :
    exitProgramWithError("Cannot connect to Telegram API.")


async def main():

    # ...
    print("TESTING: 'main' starting ...\n")





    # Verifying auth
    # if not client.is_user_authorized():
        # #exitProgramWithError("Account not authorized.")
        # client.send_code_request(phone)
        # os.system('clear')
        # banner()
        # client.sign_in(phone, input(gr+'[+] Enter the verification code: '+yo))
        # sys.exit(1)


    #me = await client.get_me()
    #print(me.stringify())


    # async with TelegramClient(name, api_id, api_hash) as client:
    result = await client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash = 0
        ))
    chats.extend(result.chats)
    
    print("\nList of chat (%d):" % (len(chats)) )
    for chat in chats:
        try:
            megaOrNot = chat.megagroup
            print(f" chat ({megaOrNot}): " + str(chat.title))
            if chat.megagroup == True or ONLY_MEGA_GROUPS == False:
                groups.append(chat)
                
        except:
            continue
    print("")
    
    
    for group in groups:
        print("Trying" + group.title)
        
        try:
        
            all_participants = []
            all_participants = await client.get_participants(group, aggressive=True)
        except:
            exitProgramWithError("You don't have the permission.")
            
    #print(''.join(groups))
    
    
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
    #print("Hello world! (2)")
            
            
    # ...
    #print("Hello world! (end)")
    
    # ...
    print("\nTESTING: 'main' ending ...\n")
    
    
    
    
    
    
    
    
#
#   executing 'main'
#

#asyncio.get_event_loop().run_until_complete(main())
#asyncio.run(main())
with client:
    client.loop.run_until_complete(main())

#task = loop.create_task(main())
#loop.run_until_complete(task)
