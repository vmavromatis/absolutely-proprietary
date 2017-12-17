import sys
import subprocess
import urllib2
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

#Get local installed packages
f1 = open("installed.txt", "w+")
f1.write(subprocess.check_output(['bash', '-c', 'pacman -Q|cut -f 1 -d " "', 'shell=True']))
f1.close()

#Get Parabola blacklist
f2 = open("blacklist.txt", "w+")
f2.write(urllib2.urlopen('https://git.parabola.nu/blacklist.git/plain/blacklist.txt').read())
f2.close()

#TODO compare lists
#
#
#
#
#
#


#Print results
cprint(figlet_format('ABSOLUTELY PROPRIETARY!', font='univers', width=160),
       'green', attrs=['bold'])
