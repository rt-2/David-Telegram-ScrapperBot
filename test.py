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
TELEGRAM_TEST_PORT = 443
TELEGRAM_PROD_IP = '149.154.167.50'
TELEGRAM_PROD_PORT = 443
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
TESTS_ONLY_MEGAGROUPS = True
TESTS_CHECK_UPDATES = True
TESTS_SHOW_BOT_SETTINGS = False
UI_SWITCH_PAGES = True
RESETBANNER_DEFAULT = -1
RESETBANNER_FORCE_CLEAR = 1
# Var(s)
asked_config = {}
last_date = None
chunk_size = 200
groups = []
chats = []
dialogs = []



#
#   Function(s)
#
# Show Banner
def resetBanner(forceCls = RESETBANNER_DEFAULT):
    # Clear terminal
    if(UI_SWITCH_PAGES or forceCls == RESETBANNER_FORCE_CLEAR):
        os.system('cls')
        # Color IN
        print(colorama.Fore.CYAN)
        # Space(s)
        print("\n")
        # App name
        print(STR_BANNER_1)
        # Credits
        print(STR_BANNER_2)
        # Color OUT
        print(colorama.Fore.RESET)
        # Space(s)
        print("\n")
        print("\n")
    
    
# Show bot settings
def printl(indentLevel, str):
    #
    spaces = " " * ((indentLevel * 4 ) + 2)
    print(spaces + str)
    
    
# Execute a UI module
async def executeModule(text, func):
    print("")
    printl(0, "%s  :" % text)
    await func()
    print("\n")
    
    
# Show bot settings
async def showBotSettings():
    #
    me = await client.get_me()
    for k, v in vars(me).items():
        printl(1, "%s:   %s ;" % (k, v))
    
    
# Show bot settings
async def getChatList():
    #
    dialogs = await client(GetDialogsRequest(
            offset_date=last_date,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chunk_size,
            hash = 0
        ))
    chats.extend(dialogs.chats)
    
    # ...
    for chat in chats:
        try:
            # Var(s)
            megaOrNot = chat.megagroup
            title = chat.title
            memberNb = chat.participants_count
            megaOrNotStr = ("Not Mega", "Mega")[megaOrNot]
            # Print(s)
            printl(1, "%s  ;" % title )
            printl(2, "(%d members, %s)" % (memberNb, megaOrNotStr) )
            #print(str(TESTS_ONLY_MEGAGROUPS) + " ;")
            # Test(s)
            if (megaOrNot == True or TESTS_ONLY_MEGAGROUPS == False) :
                # Is a mega group, or it's ignored for tests
                groups.append(chat)
                printl(4, colorama.Fore.GREEN + "ADDED")
            else :
                # Is NOT a megagroup and therefore ignored
                printl(4, colorama.Fore.RED + "EXLUDED")
        except:
            continue
    
        printl(4, colorama.Fore.RESET)
    
# Show bot settings
async def getGroupList():

    # ...
    for group in groups:
    
        group_members = []
        
        printl(1, group.title + " ;")
        #printl(1, str(group))
        
        # Test(s)
        # ...
        if(group.admin_rights == None) :
            printl(5, colorama.Fore.RED + STR_GROUP_REQUIRES_ADMIN + colorama.Fore.RESET)
        
        else :
            #printl(1, str(group.admin_rights.other) + " ;")
            
            try:
                var = True
                
                #group_members = await client.get_participants(group, aggressive=True)
            except Exception as e :
                var = True
                printl(6, e)
                #printl(5, colorama.Fore.RED + STR_GROUP_REQUIRES_ADMIN + colorama.Fore.RESET)
                
        printl(3, "Gathered %d members" % len(group_members))
        print("")
    
    

# Exit Program
def exitProgram():

    print("\nExiting program ...\n\n")
    sys.exit(1)


# Send Error
def exitProgramWithError(message):

    resetBanner()
    print("\n\nERROR:")
    print(message)
    exitProgram()


#
#   Init(s)
#
print("Initialyzing ...")
# Import(s)
import os, sys
# Var(s)
UI_SWITCH_PAGES = (UI_SWITCH_PAGES, False)[TESTS_TESTING]
TESTS_SHOW_BOT_SETTINGS = TESTS_SHOW_BOT_SETTINGS and TESTS_TESTING
#TESTS_ONLY_MEGAGROUPS = TESTS_ONLY_MEGAGROUPS and not TESTS_TESTING
TESTS_CHECK_UPDATES = (TESTS_CHECK_UPDATES , False)[TESTS_TESTING]
# Init(s)

#
#   Installs(s)
#
# ...
print("Installing requirements ...")
if TESTS_CHECK_UPDATES :
    os.system('python -m pip install telethon')
    os.system('pip install configparser')
    os.system('pip install telethon')
    os.system('pip install colorama')

#
#   Import(s)
#
import configparser
import colorama
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, ChannelParticipantAdmin


# Main/All?
async def main():

    # ...
    print("TESTING: 'main' starting ...\n")


    #
    if TESTS_SHOW_BOT_SETTINGS :
        await executeModule("Settings", showBotSettings)


    # Verifying auth
    if not await client.is_user_authorized():
        # ...
        await client.send_code_request(asked_config['phone'])
        await client.sign_in(asked_config['phone'], input('[+] Enter the verification code: '))

    resetBanner()
    
    await executeModule("List of chats (%d)" % len(chats), getChatList)

    
    resetBanner()
    
    
    await executeModule("Scraping members from choosen groups(%d)" % len(groups), getGroupList)
    
    
    # ...
    #print("\nTESTING: 'main' ending ...\n")
    
    
    

#
#   Main
#
# Init(s)
# ...
colorama.init()
# ...
resetBanner(RESETBANNER_FORCE_CLEAR)
# ...
print("Initialyzed.\n")

print("")


# Parsing config file
try:

    # ...
    print(" Parsing config file ...")
    # ...
    conf_parser = configparser.RawConfigParser()
    conf_parser.read("config.data")
    # ...
    asked_config.update(dict(conf_parser.items("cred")))
    asked_config["bot_token"] = asked_config["api_id"] + ":" + asked_config["api_hash"]
    asked_config["phone"] = asked_config["phone"].replace(" ", "").replace("-", "")
    asked_config["name"] = "testName"

    # ...
    print("\nConfigurations :")
    for k, v in asked_config.items():
        print("%s:   %s ;" % (k, v))
    print("\n")
    
    
except Exception :
    # ...
    exitProgramWithError(STR_CONFIG_FILE_ERROR)

# Connecting
try:
    # ...
    client = TelegramClient(asked_config['name'], asked_config['api_id'], asked_config['api_hash'])
    #client.session.set_dc(dc_id, '149.154.167.40', 443)
except Exception as e :
    # ...
    printl(5, e);
    exitProgramWithError(STR_CONNECTION_FAILED)

# Execute main
with client:
    #if(TESTS_TESTING): client.session.set_dc(2, TELEGRAM_TEST_IP, TELEGRAM_TEST_PORT)
    client.loop.run_until_complete(main())

# Print good bye
print(colorama.Fore.CYAN + "\nExecution over, good bye!\n")
