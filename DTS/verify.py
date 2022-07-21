import sys, os
import subprocess
import pkg_resources


#
#   Remove session files
#
dir_path = os.getcwd()
files = os.listdir(dir_path)
for file in files:
    if file.endswith(".session") or file.endswith(".session-journal"):
        os.remove(os.path.join(dir_path, file))


        
#
#   Update required librairies
#
required = {'telethon', 'configparser', 'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)