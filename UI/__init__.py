
#
#   Init(s)
#
# Import(s)
import os, sys
import DTS.verify
import colorama


#
#   Var(s)
#
# Constant(s)
RESETBANNER_DEFAULT = -1
RESETBANNER_FORCE_CLEAR = 1
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


#
#   Function(s)
#

# Show Banner
def resetBanner(forceCls = False):
    # Clear terminal
    if(os.environ["UI_SWITCH_PAGES"] == "True" or forceCls == True):
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
    







