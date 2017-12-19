import sys
import os
import subprocess
import urllib.request

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
print("Listing packages")

packages = subprocess.check_output(["pacman", "-Qq"]).decode().strip().split('\n')

if not os.path.isfile("blacklist.txt"):
    print("blacklist.txt not found, generating")
    with open("blacklist.txt", "w+") as blacklist_file:
        for url in BLACKLIST_URLS:
            print("Downloading {}".format(url))
            blacklist_file.write(urllib.request.urlopen(url).read().decode())

print("Parsing blacklist.txt")

with open("blacklist.txt") as f:
    blacklist = f.read().strip().split('\n')

print("Checking packages")

cleaned_blacklist = {}

for line in blacklist:
    name = line.split(':')[0]
    if not line:
        continue
    reason = ((line.split(':')[4]).split(']')[0]).strip().replace('[', '')
    if reason == "":
        reason = "nonfree"
    if not reason in IGNORE_REASONS:
        cleaned_blacklist[name] = reason

proprietary = 0

# Generate proprietary list
with open("disgusting.txt", "w+") as stallman_disapproves:
    for package in packages:
        package = package.strip()
        if package in cleaned_blacklist:
            stallman_disapproves.write("{}: {}\n".format(package, cleaned_blacklist[package]))
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
print("\n{0}-{1}-\n{2} ABSOLUTELY PROPRIETARY PACKAGES INSTALLED\n-{1}-{3}".format(INDEX_COLOR, "=" * 20, proprietary, RESET))
print("Your GNU/Linux is infected with {1}{3}{2} proprietary packages out of {0}{4}{2} total installed. Your Stallman Freedom Index is {1}{5:.2f}{2}"
        .format(GREEN, INDEX_COLOR, RESET, proprietary, total, stallmanfreedomindex))
print("The proprietary packages have been saved to disgusting.txt")
