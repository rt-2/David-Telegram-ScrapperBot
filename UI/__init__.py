
#
#   Init(s)
#
# Import(s)
import os, sys
import DTS.verify
from DTS import Constants

import colorama


#
#   Var(s)
#
# Constant(s)
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
    if(Constants.UI_SWITCH_PAGES == True or forceCls == True):
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
        
# Show formatted 'print'
def printl(indentLevel, str):
    str = indentText(indentLevel, str)
    return print(str)
    
# Show formatted 'input'
def inputl(indentLevel, str, color = None):
    if(color != None):
        str = color + str + colorama.Fore.RESET
    str = indentText(indentLevel, str)
    return input(str)
  
# Return indented texts
def indentText(indentLevel, str):
    spaces = " " * ((indentLevel * 4 ) + 2)
    return spaces + str



    







