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
# Import(s)
import os, sys
import DTS.verify
import DTS, UI
from DTS import Constants, Texts

import configparser
import colorama
from telethon import TelegramClient, events
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputChannel, ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError



#
#   Var(s)
#
# Constant(s)
# Var(s)
asked_config = {}



#
#   Function(s)
#    
    
    
    
#
#   Init(s)
#
# Var(s)
Constants.TESTS_SHOW_BOT_SETTINGS = Constants.TESTS_SHOW_BOT_SETTINGS and Constants.TESTS_TESTING
#Constants.TESTS_ONLY_MEGAGROUPS = (Constants.TESTS_ONLY_MEGAGROUPS, False)[Constants.TESTS_TESTING]
#Constants.UI_SWITCH_PAGES = (Constants.UI_SWITCH_PAGES, False)[Constants.TESTS_TESTING]
# Init(s)


# Main/All?
async def main():

    # ...
    print("\nTESTING: 'main' starting ...\n\n")


    #
    if Constants.TESTS_SHOW_BOT_SETTINGS :
        await DTS.executeModule("Settings", DTS.showBotSettings)


    # Verifying auth
    if not await client.is_user_authorized():
        # ...
        await client.send_code_request(asked_config['phone'])
        await client.sign_in(asked_config['phone'], input('[+] Enter the verification code: '))

    # ...
    UI.resetBanner()
    
    # ...
    chats = await DTS.executeModule("Finding list of chats", DTS.getChatList, client)

    # ...
    groups = await DTS.executeModule("Checking list of chats (%d)" % len(chats), DTS.checkChatList, chats)

    # ...
    UI.resetBanner()
    
    # ...
    #group_from = groups[0]
    group_from = await DTS.executeModule("Groupe Selection (Scraping)", DTS.chooseGroup, groups)
    #print("Group FROM is %s" % str(group_from))
    
    # ...
    #UI.resetBanner()
    
    # ...
    #group_to = groups[0]
    group_to = await DTS.executeModule("Groupe Selection (Inviting)", DTS.chooseGroup, groups)
    #print("Group TO is %s" % str(group_to))
    # Test(s)
    # ...
    if group_from.id == group_to.id:
        # ...
        DTS.exitProgramWithError(Texts.STR_GROUP_SAMENUMBER)



    # ...
    UI.resetBanner()
    
    #members = await DTS.executeModule("Scraping members from choosen groups(%d)" % len(groups), DTS.getGroupList, groups)
    
    #all_participants_from = await DTS.getMemberList(group_from)
    all_participants_from = await DTS.executeModule("Compiling members (FROM)", DTS.getMemberList, [client, group_from])
    
    all_participants_to = await DTS.executeModule("Compiling members (TO)", DTS.getMemberList, [client, group_to])
    
    #print(str(all_participants_from[0]))
    # Reverse list to start by the end
    all_participants_from.reverse()
    
    #print(str(all_participants_from[0]))
    # ...
    UI.resetBanner()

    #print(type(all_participants_from))
    
    UI.printl(0, "Compiling members  :")
    UI.printl(1, "Total members in origin groupe: %d" % len(all_participants_from))

    all_participants_final = []
    for participant in all_participants_from:
        if participant not in all_participants_to:
            all_participants_final.append(participant)
        pass
        
    UI.printl(1, "Number of members in already in destination groupe: %d" % (len(all_participants_from) - len(all_participants_final)))

    UI.printl(1, "Number of members to invite: %d" % len(all_participants_final))


    #print(len(all_participants_final ))


    # ...
    await DTS.executeModule("Inviting members", DTS.inviteAllMember, [client, all_participants_final, group_to])


        

    # ...
    #print("\n\nTESTING: 'main' ending ...\n\n")
    
    
    

#
#   Main
#
# Init(s)
# ...
colorama.init()
# ...
sys.stdout.write("\x1b]2;%s\x07" % Texts.APP_TITLE)
UI.resetBanner(True)
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
    asked_config.update(dict(conf_parser.items("creds")))
    asked_config["bot_token"] = asked_config["api_id"] + ":" + asked_config["api_hash"]
    asked_config["phone"] = asked_config["phone"].replace(" ", "").replace("-", "")
    asked_config["name"] = "testName"
    # ...
    intervals_list = dict(conf_parser.items("intervals"));
    DTS.time_all = int(intervals_list['time_all'])
    DTS.time_error = int(intervals_list['time_error'])
    DTS.time_pause = int(intervals_list['time_pause'])

    # ...
    print("\n")
    UI.printl(1, "Configurations :")
    for k, v in asked_config.items():
        UI.printl(2, "%s:   %s ;" % (k, v))
    print("\n")
    
    
except Exception :
    # ...
    DTS.exitProgramWithError(Texts.STR_CONFIG_FILE_ERROR)

# Connecting
try:
    # ...
    client = TelegramClient(asked_config['name'], asked_config['api_id'], asked_config['api_hash'])
    client.flood_sleep_threshold = 0
    #client.session.set_dc(dc_id, '149.154.167.40', 443)
except Exception as e :
    # ...
    UI.printl(5, e);
    DTS.exitProgramWithError(Texts.STR_CONNECTION_FAILED)

# Execute main
with client:
    client.loop.run_until_complete(main())
    pass

# Print good bye
print(colorama.Fore.CYAN + "\n\nExecution over, good bye!\n\n\n")
