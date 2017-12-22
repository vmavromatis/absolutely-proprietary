#!/usr/bin/env python3
import sys
import subprocess
import urllib.request
import argparse
import tempfile


def format_entry(entry, max_line_length, delim=" "):
    # accumulated line length
    ACC_length = 0
    words = entry.split(delim)
    formatted_entry = ""
    for word in words:
        # if ACC_length + len(word) and a space is <= max_line_length
        if ACC_length + (len(word) + 1) <= max_line_length:
            # append the word and a space
            formatted_entry = formatted_entry + word + delim
            # length = length + length of word + length of space
            ACC_length = ACC_length + len(word) + 1
        else:
            # append a line break, then the word and a space
            formatted_entry = formatted_entry + "\n" + word + delim
            # reset counter of length to the length of a word and a space
            ACC_length = len(word) + 1
    formatted_entry = formatted_entry[:-1]
    return formatted_entry


def line_separator(w, x, y, z):
    return "+-{:<{}}-+-{:<{}}-+-{:<{}}-+-{:<{}}-+\n" \
        .format("-" * w, w, "-" * x, x, "-" * y, y, "-" * z, z)


parser = argparse.ArgumentParser(description='Find proprietary packages')
parser.add_argument('-f', '--full', action='store_true',
                    help='Print every package not just nonfree')
parser.add_argument('-r', '--reverse', action='store_true',
                    help='Reverse the sort')
sort_group = parser.add_mutually_exclusive_group()
sort_group.add_argument('-s', '--status', action='store_true',
                        help='Sort the table by the status column')
sort_group.add_argument('-a', '--alternative', action='store_true',
                        help='Sort the table by the alternative column')
args = parser.parse_args()

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

RED = "\033[0;31m" if IS_TTY else ""
YELLOW = "\033[0;33m" if IS_TTY else ""
GREEN = "\033[0;32m" if IS_TTY else ""
RESET = "\033[0m" if IS_TTY else ""

# Get local installed packages
print("Retrieving local packages (including AUR)...")

packages = subprocess.check_output(
    ["pacman", "-Qq"]).decode().strip().split('\n')

blacklist_list = []
for url in BLACKLIST_URLS:
    print("Downloading {}".format(url))
    blacklist_list.extend(
        urllib.request.urlopen(url).read().decode().strip().split('\n'))

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
            cleaned_blacklist[name] = [reason, desc, alternatives]

proprietary = 0

# Generate proprietary list
stallman_disapproves = []
for package in packages:
    package = package.strip()
    if package in cleaned_blacklist:
        stallman_disapproves.append(
            [package, cleaned_blacklist[package][0],
             cleaned_blacklist[package][1],
             cleaned_blacklist[package][2]])
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
print("{0}{1}\n{2} ABSOLUTELY PROPRIETARY PACKAGES INSTALLED\n{1}{3}"
      .format(INDEX_COLOR, "=" * 45, proprietary, RESET))
print("\nYour GNU/Linux is infected with {0}{2}{1} proprietary packages"
      "out of {0}{3}{1} total installed.\n"
      "Your Stallman Freedom Index is {0}{4:.2f}{1}\n"
      .format(INDEX_COLOR, RESET, proprietary, total, stallmanfreedomindex))


# Leave only "nonfree" packages in list if "full" argument is not passed
if not vars(args)["full"]:
    stallman_disapproves = \
        [item for item in stallman_disapproves if item[1] == "nonfree"]

# Sort by column "status" if "status" argument is passed
if vars(args)["status"]:
    # check if "reverse" is passed
    if vars(args)["reverse"]:
        stallman_disapproves.sort(key=lambda x: x[1], reverse=True)
    else:
        stallman_disapproves.sort(key=lambda x: x[1])

# Sort by column "alternative" if "alternative" argument is passed
if vars(args)["alternative"]:
    # check if "reverse" is passed
    if vars(args)["reverse"]:
        stallman_disapproves.sort(key=lambda x: x[3], reverse=True)
    else:
        stallman_disapproves.sort(key=lambda x: x[3])

# Reverse sorting if "reverse" argument is passed
# but "status" and "alternative" is not
if vars(args)["reverse"] \
        and not vars(args)["status"] \
        and not vars(args)["alternative"]:
    stallman_disapproves.sort(reverse=True)

# Store longest element's length in each stallman_disapproves list item
package_len = 0
status_len = 0
description_len = 0
alternative_len = 0
for item in stallman_disapproves:
    # replace newline characters with nothing
    item[0] = item[0].replace("\n", "")
    item[1] = item[1].replace("\n", "")
    item[2] = item[2].replace("\n", "")
    item[3] = item[3].replace("\n", "")
    if len(item[0]) > package_len:
        package_len = len(item[0])
    if len(item[1]) > status_len:
        status_len = len(item[1])
    if len(item[2]) > description_len:
        description_len = len(item[2])
    if len(item[3]) > alternative_len:
        alternative_len = len(item[3])

# Create a temporary file
_, tmp_file = tempfile.mkstemp()
with open(tmp_file, "w") as f:
    # Print first horizontal separator of table
    f.write(line_separator(package_len,
                           status_len,
                           description_len,
                           alternative_len))
    # Print rest of the table
    for item in stallman_disapproves:
        # print element
        f.write("| {:<{}} | {:<{}} | {:<{}} | {:<{}} |\n"
                .format(item[0], package_len,
                        item[1], status_len,
                        item[2], description_len,
                        item[3], alternative_len))
        # print horizontal separator
        f.write(line_separator(package_len,
                               status_len,
                               description_len,
                               alternative_len))
# Disable CLI line wrapping
subprocess.call(["setterm", "-linewrap", "off"])
subprocess.call(["cat", tmp_file])

save_it = input("\nSave list to file? (Y/n) ")
if "n" in save_it.lower():
    subprocess.call(["rm", "-f", tmp_file])
else:
    print("The list is saved at", tmp_file)
    print("\nYou can review it from the command line\n"
          "using the \"less -S {0}\"\n"
          "or, if installed, the \"most {0}\" commands".format(tmp_file))
