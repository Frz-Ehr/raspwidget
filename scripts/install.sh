#!/bin/bash

# Make the scripts executable
find $HOME/raspwidget -name "*.sh" -o -name "*.py" -exec chmod +x {} \;

# Create the .desktop file
echo "[Desktop Entry]
Type=Application
Name=UpdateRaspwidget
Exec=sh -c '$HOME/update.sh'
Icon=$HOME/src/update-icone.png
Terminal=false" > $HOME/Desktop/UpdateRaspwidget.desktop

# Make the .desktop file executable
chmod +x $HOME/Desktop/UpdateRaspwidget.desktop
