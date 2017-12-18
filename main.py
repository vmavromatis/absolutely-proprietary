from __future__ import division
import sys
import subprocess
import urllib2
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

#Get local installed packages
f1 = open("installed.txt", "w+")
f1.write(subprocess.check_output(['bash', '-c', 'pacman -Qq', 'shell=True']))
f1.close()

#Get Parabola blacklist
f2 = open("blacklist.txt", "w+")
f2.write(urllib2.urlopen('https://git.parabola.nu/blacklist.git/plain/blacklist.txt').read())
f2.close()

#Generate proprietary list
f3 = open("disgusting.txt", "w+")

#Compare lists
countproprietary=0
with open('installed.txt') as installed:
    for package in installed:
        package = package.strip()
        with open("blacklist.txt") as f:
            for line in f:
                # Find package names in blacklist
                real_pkg_name = line.split(':')[0]
                reason = ((line.split(':')[4]).split(']')[0]+"]").strip()

                if real_pkg_name == package:
                    f3.write(package+" > "+reason+"\n")
                    countproprietary +=1
                    break
f3.close()

#Print results
cprint(figlet_format(('%s ABSOLUTELY PROPRIETARY PACKAGES' % (countproprietary)), font='univers', width=160),
        'green', attrs=['bold'])

total=int(subprocess.check_output(['bash', '-c', 'pacman -Q | wc -l', 'shell=True']))
stallmanfreedomindex=(total-countproprietary)*100/total
print("Your GNU/Linux is infected with %s proprietary packages out of %s total installed. Your Stallman Freedom Index is %.2f.\n") % (countproprietary,total,stallmanfreedomindex)
print("The proprietary packages have been saved as /tmp/absolutely-proprietary/disgusting.txt")
