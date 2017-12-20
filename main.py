import sys
import subprocess
import urllib.request
import re
from prettytable import PrettyTable

def format_entry(entry, max_line_length, delim=" "):
    #accumulated line length
    ACC_length = 0
    words = entry.split(delim)
    formatted_entry = ""
    for word in words:
        #if ACC_length + len(word) and a space is <= max_line_length
        if ACC_length + (len(word) + 1) <= max_line_length:
            #append the word and a space
            formatted_entry = formatted_entry + word + delim
            #length = length + length of word + length of space
            ACC_length = ACC_length + len(word) + 1
        else:
            #append a line break, then the word and a space
            formatted_entry = formatted_entry + "\n" + word + delim
            #reset counter of length to the length of a word and a space
            ACC_length = len(word) + 1
    formatted_entry = formatted_entry[:-1]
    return formatted_entry

BLACKLIST_URLS = [
    "https://git.parabola.nu/blacklist.git/plain/blacklist.txt",
    "https://git.parabola.nu/blacklist.git/plain/aur-blacklist.txt"
]

IGNORE_REASONS = [
    "FIXME",
    "branding",
    "technical"
]

IS_TTY = sys.stdout.isatty()

RED = "\033[1;31m" if IS_TTY else ""
YELLOW = "\033[1;33m" if IS_TTY else ""
GREEN = "\033[1;32m" if IS_TTY else ""
RESET = "\033[0m" if IS_TTY else ""

# Get local installed packages
print("Retrieving local packages (including AUR)...")

packages = subprocess.check_output(["pacman", "-Qq"]).decode().strip().split('\n')

blacklist_list = []
for url in BLACKLIST_URLS:
    print("Downloading {}".format(url))
    blacklist_list.extend(urllib.request.urlopen(url).read().decode().strip().split('\n'))

blacklist_list = [bl for bl in blacklist_list if len(bl) > 0]
print("Comparing local packages to remote...")

cleaned_blacklist = {}

for line in blacklist_list:
    if len(line) > 0:
        splitted = line.split(':')

        name = splitted[0]
        reason = ((line.split(':')[4]).split(']')[0]).strip().replace('[', '')

        alternatives = []
        for alt in splitted[1:]:
            if len(alt) > 0 and "[" not in alt:
                alternatives.append(alt.strip())
            else:
                break
        if len(alternatives) > 0:
            alternatives = ','.join(alternatives)
            alternatives = format_entry(alternatives, 30, ",")
        else:
            alternatives = ''

        desc = ''
        reason_index = line.find(reason + "]")
        if reason_index != -1:
            desc = line[reason_index + len(reason) + 1:]
            desc = desc.strip()

        desc = format_entry(desc, 90)

        if reason == "":
            reason = "nonfree"
        if not reason in IGNORE_REASONS:
            cleaned_blacklist[name] = [reason, alternatives, desc]

proprietary = 0

# Generate proprietary list
stallman_disapproves = []
for package in packages:
    package = package.strip()
    if package in cleaned_blacklist:
        stallman_disapproves.append([package, cleaned_blacklist[package][0], cleaned_blacklist[package][1], cleaned_blacklist[package][2]])
        proprietary += 1

total = len(packages)
stallmanfreedomindex = (total - proprietary) * 100 / total

if stallmanfreedomindex > 95:
    INDEX_COLOR = GREEN
elif stallmanfreedomindex > 25:
    INDEX_COLOR = YELLOW
else:
    INDEX_COLOR = RED

# Print results
print("{0}{1}\n{2} ABSOLUTELY PROPRIETARY PACKAGES INSTALLED\n{1}{3}".format(INDEX_COLOR, "=" * 45, proprietary, RESET))
print("\nYour GNU/Linux is infected with {1}{3}{2} proprietary packages out of {0}{4}{2} total installed.\nYour Stallman Freedom Index is {1}{5:.2f}{2}\n"
        .format(GREEN, INDEX_COLOR, RESET, proprietary, total, stallmanfreedomindex))

table = PrettyTable(['Name', 'Status', 'Alternatives', 'Description'])
for package in stallman_disapproves:
    table.add_row(package)

print(table)
