
#
#   Init(s)
#
# Import(s)
import os, sys
import DTS.verify

import UI
import colorama
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, ChannelParticipantAdmin


#
#   Var(s)
#
# Constant(s)
DIALOGREQ_LASTDATE = None
DIALOGREQ_CHUNKSIZE = 200
# Var(s)

#
#   Function(s)
#

# Execute a UI module
async def executeModule(text, func, arg1 = None):
    print("")
    UI.printl(0, "%s  :" % text)

    if(arg1 == None):
        ret = await func()
    else:
        ret = await func(arg1)


    print("\n")
    return ret




    
# Show bot settings
async def showBotSettings():
    #
    me = await client.get_me()
    for k, v in vars(me).items():
        UI.printl(1, "%s:   %s ;" % (k, v))
    

# Get chat list
async def getChatList(client):
    #
    chats = []
    #
    dialogs = await client(GetDialogsRequest(
            offset_date=DIALOGREQ_LASTDATE,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=DIALOGREQ_CHUNKSIZE,
            hash = 0
        ))
    chats.extend(dialogs.chats)
    
    UI.printl(1, "Found %d chats .." % len(chats) )

    return chats
    
# Check chat list
async def checkChatList(chats):
    
    # ...
    groups = []
    # ...
    for chat in chats:
    
        # ...
        print("")

        try:
            # Var(s)
            megaOrNot = chat.megagroup
            title = chat.title
            memberNb = chat.participants_count
            megaOrNotStr = ("Not Mega", "Mega")[megaOrNot]
            # Print(s)
            UI.printl(1, "%s  ;" % title )
            UI.printl(2, "(%d members, %s)" % (memberNb, megaOrNotStr) )
            #print(str(chat) + " ;")
            # Test(s)
            if (megaOrNot == True or os.environ["TESTS_ONLY_MEGAGROUPS"] == "False") :
                #print(" Yes ;")
                # Is a mega group, or it's ignored for tests
                groups.append(chat)
                UI.printl(4, colorama.Fore.GREEN + "ADDED")
            else :
                #print(" No ;")
                # Is NOT a megagroup and therefore ignored
                UI.printl(4, colorama.Fore.RED + "EXLUDED")
        except:
            pass
    
        UI.printl(4, colorama.Fore.RESET)

    return groups
    
# Get group list
async def getGroupList(groups):

    # ...
    for group in groups:
    
        # ...
        print("")

        group_members = []
        
        UI.printl(1, group.title + " ;")
        UI.printl(1, str(group))
        
        # Test(s)
        # ...
        if(group.admin_rights == None) :
            UI.printl(5, colorama.Fore.RED + STR_GROUP_REQUIRES_ADMIN + colorama.Fore.RESET)
        
        else :
            #UI.printl(1, str(group.admin_rights.other) + " ;")
            
            try:
                var = True
                
                #group_members = await client.get_participants(group, aggressive=True)
            except Exception as e :
                var = True
                printl(6, e)
                #UI.printl(5, colorama.Fore.RED + STR_GROUP_REQUIRES_ADMIN + colorama.Fore.RESET)
                
        UI.printl(3, "Gathered %d members" % len(group_members))
        print("")

    return group_members

    
# Group selection
async def chooseGroup(groups):

    # ...
    UI.printl(1, 'Choose a group :')
    for i, g in enumerate(groups):
        UI.printl(2, '[ %d ] - %s ;' % (i, g.title))
    print('')

    # ...
    while(True):
        # ...
        asked_groupid = UI.inputl(1, "Enter a Group ID: ", colorama.Fore.RED)

        try:
            groupid = int(asked_groupid)

            #print("len is %d" % len(groups))
            if(groupid < len(groups) and groupid >= 0):
                # ...
                ret = groups[groupid]
                break
        except:
            pass

        UI.printl(2, os.environ["STR_GROUP_INVALIDNUMBER"])

    return ret

    
    

# Exit Program
def exitProgram():

    print("\nExiting program ...\n\n")
    sys.exit(1)


# Send Error
def exitProgramWithError(message):

    UI.resetBanner()
    print("\n\nERROR:")
    print(message)
    exitProgram()






