# Absolutely Proprietary
Proprietary package detector. Compares your installed packages against Parabola's package blacklist and then prints your Stallman Freedom Index.

# Quick install & run
### Python 3
`sudo pacman -S python python-pip --needed && cd /tmp && git clone https://github.com/vmavromatis/absolutely-proprietary.git && cd absolutely-proprietary && sudo pip install -r requirements.txt && python main.py`
### Python 2
`sudo pacman -S python2 python2-pip --needed && cd /tmp && git clone https://github.com/vmavromatis/absolutely-proprietary.git && cd absolutely-proprietary && sudo pip2 install -r requirements.txt && python2 main.py`

Once done, you may run `less /tmp/absolutely-proprietary/disgusting.txt` to view the detailed results. Explanation of terms:
- *[nonfree]*: This package is blatantly nonfree software. 
- *[semifree]*: This package is mostly free, but contains some nonfree software.
- *[uses-nonfree]*: This package depends on, recommends, or otherwise inappropriately integrates with other nonfree software or services.

# Dependencies
### Python 3
* `python` and `python-pip`.
* `colorama`, `termcolor`, `pyfiglet` and `wget`.
### Python 2
* `python2` and `python2-pip`.
* `colorama`, `termcolor`, `pyfiglet` and `wget`.

After installing Python, install dependencies: `pip install -r requirements.txt` or `pip2 install -r requirements.txt` depending on your Python version.

# Example output
```
        ,d8  ad88888ba            db        88888888ba   ad88888ba    ,ad8888ba,   88         88        88 888888888888 88888888888 88     8b        d8  
      ,d888 d8"     "88          d88b       88      "8b d8"     "8b  d8"'    `"8b  88         88        88      88      88          88      Y8,    ,8P   
    ,d8" 88 8P       88         d8'`8b      88      ,8P Y8,         d8'        `8b 88         88        88      88      88          88       Y8,  ,8P    
  ,d8"   88 Y8,    ,d88        d8'  `8b     88aaaaaa8P' `Y8aaaaa,   88          88 88         88        88      88      88aaaaa     88        "8aa8"     
,d8"     88  "PPPPPP"88       d8YaaaaY8b    88""""""8b,   `"""""8b, 88          88 88         88        88      88      88"""""     88         `88'      
8888888888888        8P      d8""""""""8b   88      `8b         `8b Y8,        ,8P 88         88        88      88      88          88          88       
         88 8b,    a8P      d8'        `8b  88      a8P Y8a     a8P  Y8a.    .a8P  88         Y8a.    .a8P      88      88          88          88       
         88 `"Y8888P'      d8'          `8b 88888888P"   "Y88888P"    `"Y8888Y"'   88888888888 `"Y8888Y"'       88      88888888888 88888888888 88       
                                                                                                                                                         
                                                                                                                                                         
                                                                                                                                
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
                                                                                                       
                                                                                                       

Your GNU/Linux is infected with 49 proprietary packages out of 1084 total installed. Your Stallman Freedom Index is 95.48.

The proprietary packages have been saved as /tmp/absolutely-proprietary/disgusting.txt
```
