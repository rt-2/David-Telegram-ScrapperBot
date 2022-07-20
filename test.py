# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @AbirHasan2005
#   and used by @rt-2
# Telegram Group: http://t.me/linux_repo
# Please give me credits if you use any codes from here.


#
#   Init(s)
#
print("Initialyzing ...")
import DTS.verify
# Import(s)
import os, sys
import DTS, UI


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
TESTS_ONLY_MEGAGROUPS = True
TESTS_CHECK_UPDATES = True
TESTS_SHOW_BOT_SETTINGS = False
os.environ["UI_SWITCH_PAGES"] = "True"
# Var(s)
asked_config = {}



#
#   Function(s)
#    
    
    
    
#
#   Init(s)
#
# Var(s)
TESTS_SHOW_BOT_SETTINGS = TESTS_SHOW_BOT_SETTINGS and TESTS_TESTING
#TESTS_ONLY_MEGAGROUPS = TESTS_ONLY_MEGAGROUPS and not TESTS_TESTING
TESTS_CHECK_UPDATES = (TESTS_CHECK_UPDATES , False)[TESTS_TESTING]
os.environ["UI_SWITCH_PAGES"] = ("True", "False")[TESTS_TESTING]
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


# Main/All?
async def main():

    # ...
    print("\nTESTING: 'main' starting ...\n\n")


    #
    if TESTS_SHOW_BOT_SETTINGS :
        await DTS.executeModule("Settings", DTS.showBotSettings)


    # Verifying auth
    if not await client.is_user_authorized():
        # ...
        await client.send_code_request(asked_config['phone'])
        await client.sign_in(asked_config['phone'], input('[+] Enter the verification code: '))

    UI.resetBanner()
    
    chats = await DTS.executeModule("Finding list of chats", DTS.getChatList, client)

    groups = await DTS.executeModule("Checking list of chats (%d)" % len(chats), DTS.checkChatList, chats)

    
    UI.resetBanner()
    
    
    await DTS.executeModule("Scraping members from choosen groups(%d)" % len(groups), DTS.getGroupList, groups)
    
    
    # ...
    #print("\n\nTESTING: 'main' ending ...\n\n")
    
    
    

#
#   Main
#
# Init(s)
# ...
colorama.init()
# ...
UI.resetBanner(UI.RESETBANNER_FORCE_CLEAR)
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
    DTS.exitProgramWithError(STR_CONFIG_FILE_ERROR)

# Connecting
try:
    # ...
    client = TelegramClient(asked_config['name'], asked_config['api_id'], asked_config['api_hash'])
    #client.session.set_dc(dc_id, '149.154.167.40', 443)
except Exception as e :
    # ...
    UI.printl(5, e);
    DTS.exitProgramWithError(STR_CONNECTION_FAILED)

# Execute main
with client:
    #if(TESTS_TESTING): client.session.set_dc(2, TELEGRAM_TEST_IP, TELEGRAM_TEST_PORT)
    client.loop.run_until_complete(main())
    pass

# Print good bye
print(colorama.Fore.CYAN + "\n\nExecution over, good bye!\n\n\n")
