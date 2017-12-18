# Absolutely Proprietary
Compare your installed packages against Parabola's package blacklist

# Dependencies
* Python 2
* `colorama`, `termcolor`, and `pyfiglet`.

After installing Python 2, install dependencies: `pip install -r requirements.txt`

# Example output
```
discover::::[uses-nonfree][FIXME:package] depends on nonfree archlinux-appstream-data

gnome-software::parabola:1413:[uses-nonfree][FIXME:package] depends on nonfree archlinux-appstream-data

atom::::[uses-nonfree] depends on nonfree electron

caprine::::[uses-nonfree] depends on nonfree electron

messengerfordesktop::::[uses-nonfree] depends on nonfree electron

min::parabola:1204:[uses-nonfree] has non-privacy search engines, depends on nonfree electron

riot-desktop::parabola:1380:[uses-nonfree] depends on nonfree electron

cinelerra-cv::::[uses-nonfree] needs nonfree faac

gst-plugins-bad:gst-plugins-bad:::[uses-nonfree] depends on nonfree package faac

libquicktime:libquicktime:::[uses-nonfree] depends on faac

mencoder:mencoder:::[uses-nonfree] depends on nonfree package faac, Parabola use mencoder, without dependency of faac

mplayer:mplayer:::[uses-nonfree] depends on nonfree package faac, Parabola use mplayer, without dependency of faac

mplayer-vaapi:mplayer-vaapi:::[uses-nonfree] depends on faac

iscan::parabola:705:[nonfree] contains a nonfree shared library called esmod inside the source distribution which is used by the program's GUI, apart from that it also recommends nonfree plugins in the README file

deepin-game::parabola:849:[uses-nonfree] depends on nonfree flashplugin

licenses:licenses:::[use-nonfree] contains non copyleft friendly licenses

nvidia-dkms::parabola:825:[uses-nonfree] depends on nonfree package nvidia-utils

nvidia-settings::::[uses-nonfree] depends on nonfree package nvidia-utils

unace::::[nonfree] license forbids making competing ACE archivers from unace

ark:ark:::[uses-nonfree] recommends nonfree unrar

calibre:calibre:::[semifree] contains nonfree unrar

clamav:clamav::::[semifree] has nonfree unrar support for RAR into libclamunrar

lesspipe:lesspipe:::[semifree] recommends nonfree unrar

p7zip:p7zip:::[semifree] contains nonfree unrar

python2-unrardll::::[uses-nonfree] depends on nonfree libunrar

python-unrardll::::[uses-nonfree] depends on nonfree libunrar

xarchiver:xarchiver:::[uses-nonfree] recommends nonfree unrar

xarchiver-gtk2:xarchiver-gtk2:::[uses-nonfree] recommends nonfree unrar

                                                                                                                                                         
 ad888888b,  ad88888ba            db        88888888ba   ad88888ba    ,ad8888ba,   88         88        88 888888888888 88888888888 88     8b        d8  
d8"     "88 d8"     "8b          d88b       88      "8b d8"     "8b  d8"'    `"8b  88         88        88      88      88          88      Y8,    ,8P   
        a8P Y8a     a8P         d8'`8b      88      ,8P Y8,         d8'        `8b 88         88        88      88      88          88       Y8,  ,8P    
     ,d8P"   "Y8aaa8P"         d8'  `8b     88aaaaaa8P' `Y8aaaaa,   88          88 88         88        88      88      88aaaaa     88        "8aa8"     
   a8P"      ,d8"""8b,        d8YaaaaY8b    88""""""8b,   `"""""8b, 88          88 88         88        88      88      88"""""     88         `88'      
 a8P'       d8"     "8b      d8""""""""8b   88      `8b         `8b Y8,        ,8P 88         88        88      88      88          88          88       
d8"         Y8a     a8P     d8'        `8b  88      a8P Y8a     a8P  Y8a.    .a8P  88         Y8a.    .a8P      88      88          88          88       
88888888888  "Y88888P"     d8'          `8b 88888888P"   "Y88888P"    `"Y8888Y"'   88888888888 `"Y8888Y"'       88      88888888888 88888888888 88       
                                                                                                                                                         
                                                                                                                                                         
                                                                                                                                
88888888ba  88888888ba    ,ad8888ba,   88888888ba  88888888ba  88 88888888888 888888888888   db        88888888ba 8b        d8  
88      "8b 88      "8b  d8"'    `"8b  88      "8b 88      "8b 88 88               88       d88b       88      "8b Y8,    ,8P   
88      ,8P 88      ,8P d8'        `8b 88      ,8P 88      ,8P 88 88               88      d8'`8b      88      ,8P  Y8,  ,8P    
88aaaaaa8P' 88aaaaaa8P' 88          88 88aaaaaa8P' 88aaaaaa8P' 88 88aaaaa          88     d8'  `8b     88aaaaaa8P'   "8aa8"     
88""""""'   88""""88'   88          88 88""""""'   88""""88'   88 88"""""          88    d8YaaaaY8b    88""""88'      `88'      
88          88    `8b   Y8,        ,8P 88          88    `8b   88 88               88   d8""""""""8b   88    `8b       88       
88          88     `8b   Y8a.    .a8P  88          88     `8b  88 88               88  d8'        `8b  88     `8b      88       
88          88      `8b   `"Y8888Y"'   88          88      `8b 88 88888888888      88 d8'          `8b 88      `8b     88       
                                                                                                                                
                                                                                                                                
                                                                                                       
88888888ba     db        ,ad8888ba,  88      a8P         db        ,ad8888ba,  88888888888 ad88888ba   
88      "8b   d88b      d8"'    `"8b 88    ,88'         d88b      d8"'    `"8b 88         d8"     "8b  
88      ,8P  d8'`8b    d8'           88  ,88"          d8'`8b    d8'           88         Y8,          
88aaaaaa8P' d8'  `8b   88            88,d88'          d8'  `8b   88            88aaaaa    `Y8aaaaa,    
88""""""'  d8YaaaaY8b  88            8888"88,        d8YaaaaY8b  88      88888 88"""""      `"""""8b,  
88        d8""""""""8b Y8,           88P   Y8b      d8""""""""8b Y8,        88 88                 `8b  
88       d8'        `8b Y8a.    .a8P 88     "88,   d8'        `8b Y8a.    .a88 88         Y8a     a8P  
88      d8'          `8b `"Y8888Y"'  88       Y8b d8'          `8b `"Y88888P"  88888888888 "Y88888P"   
                                                                                                       
                                                                                                       

28 proprietary out of 1084 total installed. Your Stallman Freedom index is 97.42
```
