from __future__ import division
import sys
import subprocess
import urllib2
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
import re

#Get local installed packages
f1 = open("installed.txt", "w+")
f1.write(subprocess.check_output(['bash', '-c', 'pacman -Qq', 'shell=True']))
f1.close()

#Get Parabola blacklist
f2 = open("blacklist.txt", "w+")
f2.write(urllib2.urlopen('https://git.parabola.nu/blacklist.git/plain/blacklist.txt').read())
f2.close()

#FIXME comparison not working well - Compare lists
countproprietary=0
with open('installed.txt') as installed:
    for package in installed:
        package = package.strip()
        with open("blacklist.txt") as f:
            for line in f:
                # Find package names in blacklist
                stripped = re.match('.*:\s*\[', line)
                if stripped is not None:
                    real_pkg_name = stripped.group(0)

                # Escape characters which could couse problems as pattern
                regex = ''
                for c in package:
                    if c in '+':
                        regex += '\\'

                    regex += c

                # Find the package in the blacklist
                matched = re.match(r'\b' + regex + r'\b', real_pkg_name)
                if matched is not None:
                    print (line)
                    countproprietary +=1
                    break

#Print results
cprint(figlet_format(('%s ABSOLUTELY PROPRIETARY PACKAGES' % (countproprietary)), font='univers', width=160),
        'green', attrs=['bold'])

total=int(subprocess.check_output(['bash', '-c', 'pacman -Q | wc -l', 'shell=True']))
stallmanfreedomindex=(total-countproprietary)*100/total
print ("%s proprietary out of %s total installed. Your Stallman Freedom index is %.2f") % (countproprietary,total,stallmanfreedomindex)