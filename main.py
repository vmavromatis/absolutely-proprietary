#!/usr/bin/env python3
import sys
import os
import subprocess
import urllib.request
import argparse
import tempfile


def table_separator(w, x, y, z):
    return "+-{:<{}}-+-{:<{}}-+-{:<{}}-+-{:<{}}-+\n" \
        .format("-" * w, w, "-" * x, x, "-" * y, y, "-" * z, z)


def table_row(i1, l1, i2, l2, i3, l3, i4, l4):
    return "| {:<{}} | {:<{}} | {:<{}} | {:<{}} |\n" \
        .format(i1, l1, i2, l2, i3, l3, i4, l4)


def as_normal(head_name, head_status, head_alternative, head_description,
              pac_len, stat_len, alt_len, desc_len,
              stl_disapproves):
    # First horizontal separator of table
    ret = table_separator(pac_len, stat_len, alt_len, desc_len)
    # Header
    ret += table_row(head_name, pac_len,
                     head_status, stat_len,
                     head_alternative, alt_len,
                     head_description, desc_len)
    ret += table_separator(pac_len,
                           stat_len,
                           alt_len,
                           desc_len)

    # Rest of the table
    for item in stl_disapproves:
        first = True
        if len(item[2]) > 0:
            # let each alternative package name have its own line
            for s in item[2]:
                if first:
                    ret += table_row(item[0], pac_len,
                                     item[1], stat_len,
                                     s, alt_len,
                                     item[3], desc_len)
                    first = False
                else:
                    ret += table_row("", pac_len,
                                     "", stat_len,
                                     s, alt_len,
                                     "", desc_len)
        else:
            ret += table_row(item[0], pac_len,
                             item[1], stat_len,
                             "", alt_len,
                             item[3], desc_len)
        # Horizontal separator
        ret += table_separator(pac_len,
                               stat_len,
                               alt_len,
                               desc_len)
    return ret


def as_markdown_header(h1, h2, h3, h4):
    return "|{}|{}|{}|{}|  \n" \
           "|---|---|---|---|  \n" \
           .format(h1, h2, h3, h4)


def as_markdown_body(w, x, y, z):
    return "|{}|{}|{}|{}|  \n".format(w, x, y, z)


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
        desc = ''
        reason_index = line.find(reason + "]")
        if reason_index != -1:
            desc = line[reason_index + len(reason) + 1:]
            desc = desc.strip()
        if reason == "":
            reason = "nonfree"
        if reason not in IGNORE_REASONS:
            cleaned_blacklist[name] = [reason, alternatives, desc]

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
        stallman_disapproves.sort(key=lambda x: x[2], reverse=True)
    else:
        stallman_disapproves.sort(key=lambda x: x[2])

# Reverse sorting if "reverse" argument is passed
# but "status" and "alternative" is not
if vars(args)["reverse"] \
        and not vars(args)["status"] \
        and not vars(args)["alternative"]:
    stallman_disapproves.sort(reverse=True)

# Store longest element's length in each stallman_disapproves list item
# starting values set to header elements
header_name = "Name"
header_status = "Status"
header_description = "Description"
header_alternative = "Libre Alternatives"
package_len = len(header_name)
status_len = len(header_status)
description_len = len(header_description)
alternative_len = len(header_alternative)
for item in stallman_disapproves:
    if len(item[0]) > package_len:
        package_len = len(item[0])
    if len(item[1]) > status_len:
        status_len = len(item[1])
    for sub in item[2]:
        if len(sub) > alternative_len:
            alternative_len = len(sub)
    if len(item[3]) > description_len:
        description_len = len(item[3])

result = as_normal(header_name, header_status, header_alternative,
                   header_description, package_len, status_len,
                   alternative_len, description_len, stallman_disapproves)

subprocess.call(["setterm", "-linewrap", "off"])
print(result)

# Ask if file to be saved
save_it = input("\nSave list to file? (Y/n) ")
if "n" in save_it.lower():
    sys.exit()

# Ask if save as markdown
i = input("Save as markdown table? (Y/n) ")
if "n" in i.lower():
    markdown = False
else:
    markdown = True

# Create temporary file
_, tmp_file = tempfile.mkstemp()
if markdown:
    subprocess.call(["mv", tmp_file, tmp_file + ".md"])
    tmp_file += ".md"

# Ask for filename
new_file = input("Save it to ({}): ".format(tmp_file))
if new_file == "":
    new_file = tmp_file
else:
    # get absolute path, treat tilde as user's home folder
    new_file = os.path.abspath(os.path.expanduser(new_file))
    # leave tmp_file if user doesn't have permission to create new dir
    try:
        os.makedirs(os.path.dirname(new_file), exist_ok=True)
    except PermissionError:
        print("You don't have the right permissions!")
        new_file = tmp_file
# leave tmp_file if user doesn't have permission to create file
if tmp_file != new_file:
    try:
        if markdown:
            # save as markdown table
            if new_file[-3:] != ".md":
                new_file += ".md"
            with open(new_file, "w") as f:
                f.write(as_markdown_header(header_name,
                                           header_status,
                                           header_alternative,
                                           header_description))
                for item in stallman_disapproves:
                    alt = "<br>".join(item[2])
                    f.write(as_markdown_body(item[0], item[1], alt, item[3]))
        else:
            # save as regular file
            with open(new_file, "w") as f:
                f.write(result)
    except PermissionError:
        print("You don't have the right permissions!")
        # save temporary file on permission error
        new_file = tmp_file
        if markdown:
            # as markdown
            with open(new_file, "w") as f:
                f.write(as_markdown_header(header_name,
                                           header_status,
                                           header_alternative,
                                           header_description))
                for item in stallman_disapproves:
                    alt = "<br>".join(item[2])
                    f.write(as_markdown_body(item[0], item[1], alt, item[3]))
        else:
            # as regular file
            with open(new_file, "w") as f:
                f.write(result)
else:
    if markdown:
        with open(new_file, "w") as f:
            f.write(as_markdown_header(header_name,
                                       header_status,
                                       header_alternative,
                                       header_description))
            for item in stallman_disapproves:
                alt = "<br>".join(item[2])
                f.write(as_markdown_body(item[0], item[1], alt, item[3]))
    else:
        with open(new_file, "w") as f:
            f.write(result)

# Delete empty temporary file
if os.stat(tmp_file).st_size == 0:
    os.remove(tmp_file)

# Print save location and CLI view suggestions
print("The list is saved at", new_file)
print("\nYou can review it from the command line\n"
      "using the \"less -S {0}\"\n"
      "or, if installed, the \"most {0}\" commands".format(new_file))
