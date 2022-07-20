# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @AbirHasan2005
#   and used by @rt-2
# Telegram Group: http://t.me/linux_repo
# Please give me credits if you use any codes from here.


#
#   Var(s)
#
# Constant(s)
TESTS_TESTING = True
TELEGRAM_TEST_IP = '149.154.167.40'
TELEGRAM_TEST_PORT = 80
STR_CONFIG_FILE_ERROR = "File 'config.data' not formatted correctly."
STR_CONNECTION_FAILED = "Cannot connect to Telegram API."
STR_GROUP_REQUIRES_ADMIN = "This group requires admin access (ERROR)"
STR_BANNER_1 = f"""            
        ____              _     ___          ______     __     ____        __ 
       / __ \____ __   __(_)___/ ( )_____   /_  __/__  / /__  / __ )____  / /_
      / / / / __ `/ | / / / __  /|// ___/    / / / _ \/ / _ \/ __  / __ \/ __/
     / /_/ / /_/ /| |/ / / /_/ /  (__  )    / / /  __/ /  __/ /_/ / /_/ / /_  
    /_____/\__,_/ |___/_/\__,_/  /____/    /_/  \___/_/\___/_____/\____/\__/  
                                                                            """
STR_BANNER_2 = f"""             _                     _       ____  
            | |__  _   _      _ __| |_    |___ \ 
            | '_ \| | | |    | '__| __|____ __) |
            | |_) | |_| |    | |  | ||_____/ __/ 
            |_.__/ \__, |    |_|   \__|   |_____|
                   |___/                      
	"""
TESTS_ONLY_MEGAGROUPS = not TESTS_TESTING
TESTS_CHECK_UPDATES = not TESTS_TESTING
UI_SWITCH_PAGES = True
UI_SWITCH_PAGES = (UI_SWITCH_PAGES , False)[TESTS_TESTING]
CLSANDSHOWBANNER_FORCECLS_FALSE = 0
CLSANDSHOWBANNER_FORCECLS_TRUE = 1
# Var(s)
api_id = None
api_hash = None
bot_token = None
phone = None
name = None
last_date = None
chunk_size = 200
groups = []
chats = []
dialogs = []

#
#   Function(s)
#
# Show Banner
def clsAndShowBanner(forceCls = CLSANDSHOWBANNER_FORCECLS_FALSE):
    # Clear terminal
    if(UI_SWITCH_PAGES or forceCls == CLSANDSHOWBANNER_FORCECLS_TRUE):
        os.system('cls')
        # Space(s)
        print("\n")
        # App name
        print(STR_BANNER_1)
        # Credits
        print(STR_BANNER_2)
        # Space(s)
        print("\n")
        print("\n")
    
# Exit Program
def exitProgram():
    print("\nExiting program ...\n\n")
    sys.exit(1)

# Send Error
def exitProgramWithError(message):
    clsAndShowBanner()
    print("\n\nERROR:")
    print(message)
    exitProgram()


#
#   Init(s)
#
# ...
import os, sys
# ...
clsAndShowBanner(CLSANDSHOWBANNER_FORCECLS_TRUE)

#
#   Installs(s)
#
print("Initialyzing ...")
# ...
print("Installing requirements ...")
if TESTS_CHECK_UPDATES :
    os.system('python3 -m pip install telethon')
    os.system('pip3 install configparser')
    os.system('pip3 install telethon')

#
#   Import(s)
#
import configparser
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty


# Main/All?
async def main():

    # ...
    #print("TESTING: 'main' starting ...\n")





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

    clsAndShowBanner()
    
    # async with TelegramClient(name, api_id, api_hash) as client:
    dialogs = await client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash = 0
        ))
    chats.extend(dialogs.chats)
    
    # ...
    print("\nList of chats (%d):" % (len(chats)) )
    print("")
    for chat in chats:
        try:
            # Var(s)
            megaOrNot = chat.megagroup
            title = chat.title
            memberNb = chat.participants_count
            megaOrNotStr = ("Not Mega", "Mega")[megaOrNot]
            # Print(s)
            print("  %s  ;" % title )
            print("    (%d members, %s)" % (memberNb, megaOrNotStr) )
            #print(str(chat) + " ;")
            # Test(s)
            if chat.megagroup == True or TESTS_ONLY_MEGAGROUPS == False :
                # Is a mega group, or it's ignored for tests
                groups.append(chat)
                print("          ADDED")
            else :
                # Is NOT a megagroup and therefore ignored
                print("          EXLUDED")
            print("")
                
                
        except:
            continue
    print("\n")
    
    clsAndShowBanner()
    
    # ...
    print("Scraping members from choosen groups(%d)  :\n" % len(groups))
    # ...
    for group in groups:
    
        group_members = []
        print(group.title + " ;")
        
        try:
        
            group_members = await client.get_participants(group, aggressive=True)
        except:
            print("    " + STR_GROUP_REQUIRES_ADMIN)
            
        print("      " + "Gathered %d members" % len(group_members))
        print("")
        
    print("\n")
    
    # ...
    #print("\nTESTING: 'main' ending ...\n")
    
    
    

#
#   Main
#
# Init(s)
# ...
clsAndShowBanner(CLSANDSHOWBANNER_FORCECLS_TRUE)
# ...
print("Initialyzed.")


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
    # ...
    exitProgramWithError(STR_CONFIG_FILE_ERROR)

# Connecting
try:
    # ...
    client = TelegramClient(name, api_id, api_hash)
except Exception :
    # ...
    exitProgramWithError(STR_CONNECTION_FAILED)


# Execute main
with client:
    client.loop.run_until_complete(main())

# Print good bye
print("\nExecution over, good bye!\n")
