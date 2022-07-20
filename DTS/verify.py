import sys
import subprocess
import pkg_resources

import UI

print("")
UI.printl(1, "Downloading requirements")

required = {'telethon', 'configparser', 'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)