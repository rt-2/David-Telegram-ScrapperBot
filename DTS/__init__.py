
#
#   Init(s)
#
# Import(s)
import os, sys
import DTS.verify
from DTS import Constants, Texts

import time, traceback, re
import UI
import colorama
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputChannel, ChannelParticipantsSearch, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantsRequest, InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, FloodWaitError, UserPrivacyRestrictedError, UserChannelsTooMuchError, UserIdInvalidError


#time_all = 1
#time_error = 1
#time_pause = 1

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
            offset_date = Constants.TELETHON_REQUEST_LASTDATE,
            offset_id = Constants.TELETHON_REQUEST_OFFSETID,
            offset_peer = InputPeerEmpty(),
            limit = Constants.TELETHON_REQUEST_CHUNKSIZE,
            hash = Constants.TELETHON_REQUEST_HASH
        ))
    chats.extend(dialogs.chats)
    
    UI.printl(1, "Found %d chats .." % len(chats) )

    return chats
    
# Check chat list
async def checkChatList(chats):
    
    # ...
    groups = []
    # ...
    print("")
    # ...
    for chat in chats:
    
        # ...

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
            if (megaOrNot == True or Constants.TESTS_ONLY_MEGAGROUPS == False) :
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
        #asked_groupid = UI.inputl(1, "Enter a Group ID: ", colorama.Fore.RED)
        asked_groupid = UI.inputl(1, "Enter a Group ID: ")

        try:
            groupid = int(asked_groupid)

            #print("len is %d" % len(groups))
            if(groupid < len(groups) and groupid >= 0):
                # ...
                ret = groups[groupid]
                break
        except:
            pass

        UI.printl(2, Texts.STR_GROUP_INVALIDNUMBER)

    return ret

    
# Get member list
async def getMemberList(args):

    # ...
    client = args[0]
    group_from = args[1]

    all_participants_from = []
    try:
        offset = 0
        limit = 200
        my_filter = ChannelParticipantsSearch('')
        #print(group_from.access_hash)

        while True:
            participants = await client(GetParticipantsRequest(InputChannel(group_from.id, group_from.access_hash), my_filter, offset, limit, Constants.TELETHON_REQUEST_HASH))
            all_participants_from.extend(participants.users)
            offset += len(participants.users)
            if len(participants.users) < limit:
                 break


        #group_members = await client(GetParticipantsRequest(InputChannel(group_from.id, group_from.access_hash), my_filter, offset, limit, 0))
        #group_members = await client.get_participants(group_from, aggressive=True)
        
        #print(str(all_participants_from))
        #print(len(all_participants_from))
        #print(str(all_participants_from[0]))
    
    except Exception as e:
        print(type(e))
        print(str(e))

    return all_participants_from;


# Get member list
async def inviteAllMember(args):

    # ...
    client = args[0]
    all_participants_from = args[1]
    group_to = args[2]


    n = 0
    for user in all_participants_from:
        n += 1
        if n % 50 == 0:
            UI.printl(2, "Waiting %d seconds ..." % DTS.time_pause, colorama.Fore.BLUE)
            time.sleep(DTS.time_pause)
            pass
        try:
            UI.printl(1, "[ %d / %d ] Adding %s %s (%d,%d) ;" % (n, len(all_participants_from), user.first_name, user.last_name, user.id, user.access_hash))
            user_to_add = InputPeerUser(user.id, user.access_hash)
            #print(str(user))
            #print(user.access_hash)
            if not Constants.TESTS_TESTING:
                await client(InviteToChannelRequest(group_to, [user_to_add]))
            #print("Waiting for 60-180 Seconds ...")
            #time.sleep(random.randrange(0, 5))
        except PeerFloodError:
            UI.printl(2, "Getting Flood Error from telegram. Script is stopping now. Waiting %d seconds" % Constants.ADDTIME_WAIT, colorama.Fore.RED)
            #time.sleep(DTS.time_error)
            exitProgramWithError("Stopping because of flood.")
        except FloodWaitError as e:
            wait_sec = e.seconds
            UI.printl(2, "Getting Flood Error from telegram. Script is stopping now.", colorama.Fore.RED)
            UI.printl(2, "Waiting, %d seconds until unban ..." % wait_sec, colorama.Fore.YELLOW)
            #time.sleep(DTS.time_error)
            time.sleep(wait_sec)
        except UserPrivacyRestrictedError:
            wait_sec = 5
            UI.printl(2, "The user's privacy settings do not allow you to do this. Skipping in %d Seconds ..." % wait_sec, colorama.Fore.YELLOW)
            time.sleep(wait_sec)
        except UserChannelsTooMuchError:
            wait_sec = 3
            UI.printl(2, "the users you tried to add is already in too many channels/supergroups. Waiting for %d Seconds ..." % wait_sec, colorama.Fore.YELLOW)
            time.sleep(wait_sec)
        except:
            traceback.print_exc()
            UI.printl(2, "Unexpected Error! ")
            continue
           
        # ...
        UI.printl(2, "Waiting %d seconds ..." % DTS.time_all, colorama.Fore.BLUE)
        time.sleep(DTS.time_all)

    
    

# Exit Program
def exitProgram():

    print("\nExiting program ...\n\n")
    sys.exit(1)


# Send Error
def exitProgramWithError(message):

    UI.resetBanner()
    print(colorama.Fore.RED + "\n\nERROR:")
    print(message + colorama.Fore.RESET)
    exitProgram()






