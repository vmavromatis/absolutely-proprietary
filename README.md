# Absolutely Proprietary
Proprietary package detector for arch-based distros. Compares your installed packages against Parabola's package [blacklist](https://git.parabola.nu/blacklist.git/plain/blacklist.txt) and [aur-blacklist](https://git.parabola.nu/blacklist.git/plain/aur-blacklist.txt) and then prints your Stallman Freedom Index (free/total).

*Update - I thought it's better to remove all the ascii stuff so there are no external libs. Thanks for the PRs!*

# Quick install & run
`curl -o - https://raw.githubusercontent.com/vmavromatis/absolutely-proprietary/master/run.sh | sh`

Explanation of terms:
- *nonfree*: This package is blatantly nonfree software.
- *semifree*: This package is mostly free, but contains some nonfree software.
- *uses-nonfree*: This package depends on, recommends, or otherwise inappropriately integrates with other nonfree software or services.

# Output
```
Retrieving local packages (including AUR)...
Downloading https://git.parabola.nu/blacklist.git/plain/blacklist.txt
Downloading https://git.parabola.nu/blacklist.git/plain/aur-blacklist.txt
Comparing local packages to remote...
=============================================
39 ABSOLUTELY PROPRIETARY PACKAGES INSTALLED
=============================================

Your GNU/Linux is infected with 39 proprietary packages out of 1090 total installed. Your Stallman Freedom Index is 96.42

archlinux-appstream-data: uses-nonfree
b43-fwcutter: uses-nonfree
cdrtools: semifree
chromium: uses-nonfree
cpupower: semifree
cups-filters: uses-nonfree
electron: semifree
faac: nonfree
file-roller: uses-nonfree
firefox: uses-nonfree
flashplugin: nonfree
gst-plugins-bad: uses-nonfree
hexchat: uses-nonfree
hplip: uses-nonfree
intel-ucode: nonfree
ipw2100-fw: nonfree
ipw2200-fw: nonfree
lib32-mesa-demos: semifree
lib32-nvidia-utils: nonfree
licenses: use-nonfree
linux-api-headers: semifree
linux-firmware: semifree
mc: uses-nonfree
mesa: uses-nonfree
mesa-demos: semifree
nvidia-utils: nonfree
p7zip: semifree
pepper-flash: nonfree
phpstorm: nonfree
pyqt5-common: uses-nonfree
python-pyqt5: uses-nonfree
sdl: semifree
teamviewer: nonfree
unace: nonfree
unrar: nonfree
unzip: semifree
visual-studio-code: nonfree
winetricks: uses-nonfree
zd1211-firmware: uses-nonfree
```
