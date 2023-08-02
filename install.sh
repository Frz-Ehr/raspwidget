#!/bin/bash

# Make the scripts executable
for file in $(find $HOME/raspwidget -name "*.sh" -o -name "*.py")
do
    chmod +x $file
done

# Install ImageTk
sudo apt-get install python3-pil.imagetk

# Create the main.desktop file
echo "[Desktop Entry]
Type=Application
Name=Raspwidget
Exec=python3 $HOME/raspwidget/main.py
Icon=$HOME/raspwidget/src/main-icone.png
Terminal=false" > $HOME/Desktop/Raspwidget.desktop

# Make the .desktop file executable
chmod +x $HOME/Desktop/Raspwidget.desktop
chmod +x $HOME/raspwidget/main.py

# Create the update.desktop file
echo "[Desktop Entry]
Type=Application
Name=UpdateRaspwidget
Exec=x-terminal-emulator -e '$HOME/raspwidget/scripts/update.sh'
Icon=$HOME/raspwidget/src/update-icone.png
Terminal=false" > $HOME/Desktop/UpdateRaspwidget.desktop

# Make the .desktop file executable
chmod +x $HOME/Desktop/UpdateRaspwidget.desktop

