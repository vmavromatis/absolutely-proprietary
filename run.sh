#!/bin/sh

sudo pacman -S python --needed
cd /tmp
if [ -d "absolutely-proprietary" ]; then
    cd absolutely-proprietary
    git pull
else
    git clone https://github.com/vmavromatis/absolutely-proprietary.git
    cd absolutely-proprietary
fi
# sudo pip install -r requirements.txt -U
python absolutely_proprietary
