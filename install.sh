#!/bin/bash

# Make the scripts executable
for file in $(find $HOME/raspwidget -name "*.sh" -o -name "*.py")
do
    chmod +x $file
done

# Create the .desktop file
echo "[Desktop Entry]
Type=Application
Name=UpdateRaspwidget
Exec=x-terminal-emulator -e '$HOME/raspwidget/scripts/update.sh'
Icon=$HOME/raspwidget/src/update-icone.png
Terminal=false" > $HOME/Desktop/UpdateRaspwidget.desktop

# Make the .desktop file executable
chmod +x $HOME/Desktop/UpdateRaspwidget.desktop
