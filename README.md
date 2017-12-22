# Absolutely Proprietary
Proprietary package detector for arch-based distros. Compares your installed packages against Parabola's package [blacklist](https://git.parabola.nu/blacklist.git/plain/blacklist.txt) and [aur-blacklist](https://git.parabola.nu/blacklist.git/plain/aur-blacklist.txt) and then prints your Stallman Freedom Index (free/total).

*Update - I thought it's better to remove all the ascii stuff so there are no external libs. Thanks for the PRs!*

# Install
`git clone https://github.com/vmavromatis/absolutely-proprietary.git`  
`cd absolutely-proprietary`
# Update
`cd absolutely-proprietary`  
`git pull https://github.com/vmavromatis/absolutely-proprietary.git`
# Run
`python main.py [arguments]`

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

Your GNU/Linux is infected with 39 proprietary packages out of 1091 total installed.
Your Stallman Freedom Index is 96.43

+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| Name                     | Status       | Description                                                                               | Libre Alternatives            |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| archlinux-appstream-data | uses-nonfree | [FIXME:package] promotes nonfree packages and Arch repositories                           |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| b43-fwcutter             | uses-nonfree | only useful to install nonfree software                                                   | b43-tools,fsf,b43-fwcutter    |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| cdrtools                 | semifree     | Apple's license binding with no clarification (apple_driver utility is nonfree)           | cdrkit                        |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| chromium                 | uses-nonfree | [technical][FIXME:package] (1) links to proprietary plugins (2) probably not entirely     |                               |
|                          |              | built from sources                                                                        |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| cpupower                 | semifree     | (linux-tools) Build from the Linux-libre kernel                                           | linux-libre-tools-cpupower    |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| cups-filters             | uses-nonfree | recommends foomatic-db-nonfree                                                            | cups-filters                  |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| electron                 | semifree     | [FIXME:package] contains embedded Chromium, recommends nonfree modules                    |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| faac                     | nonfree      | [FIXME:description] is a GPL'ed package, but has non free code that can't be distributed  |                               |
|                          |              | under the GPL                                                                             |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| file-roller              | uses-nonfree | recommends nonfree unrar and unace installation                                           | file-roller                   |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| firefox                  | uses-nonfree | Has trademark issues, recommends nonfree software and by default has non-privacy search   |                               |
|                          |              | engines                                                                                   |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| flashplugin              | nonfree      | nonfree, nondistributable, built from binary installers, etc                              |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| gst-plugins-bad          | uses-nonfree | depends on nonfree package faac                                                           | gst-plugins-bad               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| hexchat                  | uses-nonfree | Hard-codes the firefox command in some menus                                              | hexchat                       |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| hplip                    | uses-nonfree | recommends binary blobs                                                                   | hplip                         |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| intel-ucode              | nonfree      | no modification, use restrictions                                                         |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| ipw2100-fw               | nonfree      |                                                                                           |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| ipw2200-fw               | nonfree      |                                                                                           |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| lib32-mesa-demos         | semifree     | The 'pointblast' and 'spriteblast' demos are nonfree                                      | lib32-mesa-demos              |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| lib32-nvidia-utils       | nonfree      | nonfree, nondistributable, built from binary installers, etc                              |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| licenses                 | use-nonfree  | Remove non-free CC -NC and -ND licenses (also add WTFPL)                                  | licenses                      |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| linux-api-headers        | semifree     | has source containing and recommending nonfree software, [[issue444]]                     | linux-libre-api-headers       |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| linux-firmware           | semifree     | nonfree blobs and firmwares                                                               | linux-libre-firmware,fsf,     |
|                          |              |                                                                                           | linux-firmware                |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| mc                       | uses-nonfree | recommends nonfree unace, unrar and unarj optional installation                           | mc                            |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| mesa                     | uses-nonfree | (mesa) Recommends nonfree software in /etc/drirc                                          | mesa                          |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| mesa-demos               | semifree     | The 'pointblast' and 'spriteblast' demos are nonfree                                      | mesa-demos,fsf,mesademos      |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| nvidia-utils             | nonfree      | nonfree, nondistributable, built from binary installers, etc                              |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| p7zip                    | semifree     | contains nonfree unrar                                                                    | p7zip                         |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| pepper-flash             | nonfree      | proprietary Adobe Computer Software License Agreement, missing sources                    |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| phpstorm                 | nonfree      |                                                                                           |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| pyqt5-common             | uses-nonfree | depends on nonfree qt5-webengine                                                          | pyqt5-common                  |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| python-pyqt5             | uses-nonfree | depends on nonfree qt5-webengine                                                          | python-pyqt5                  |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| sdl                      | semifree     | contains a source file that doesn't mention modification                                  | sdl                           |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| teamviewer               | nonfree      |                                                                                           |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| unace                    | nonfree      | license forbids making competing ACE archivers from unace                                 |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| unrar                    | nonfree      |                                                                                           | unar,fsf,unrar                |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| unzip                    | semifree     | contains a source file that doesn't mention modification                                  | unzip                         |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| visual-studio-code       | nonfree      |                                                                                           |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| winetricks               | uses-nonfree | recommends and installs nonfree software                                                  | winetricks-libre,parabola,366 |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+
| zd1211-firmware          | uses-nonfree | it's free, but drivers are propietary and it's not included in linux-libre                |                               |
+--------------------------+--------------+-------------------------------------------------------------------------------------------+-------------------------------+

```
