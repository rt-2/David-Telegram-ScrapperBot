
#
#   Init(s)
#
# Import(s)
import os, sys
import DTS.verify
from DTS import Constants, Texts

import colorama


#
#   Var(s)
#
# Constant(s)


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
        print(Texts.STR_BANNER_1)
        # Credits
        print(Texts.STR_BANNER_2)
        # Color OUT
        print(colorama.Fore.RESET)
        # Space(s)
        print("\n")
        print("\n")
        
# Show formatted 'print'
def printl(indentLevel, str, color = None):
    if(color != None):
        str = color + str + colorama.Fore.RESET
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



    







