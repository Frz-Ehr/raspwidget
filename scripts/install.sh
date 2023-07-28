#!/bin/bash

# Make the scripts executable
find $HOME/raspwidget -name "*.sh" -o -name "*.py" -exec chmod +x {} \;

# Create the .desktop file
echo "[Desktop Entry]
Type=Application
Name=UpdateRaspwidget
Exec=/path/to/your/update.sh
Icon=/path/to/your/icon.png
Terminal=false" > ~/Desktop/UpdateRaspwidget.desktop

# Make the .desktop file executable
chmod +x ~/Desktop/UpdateRaspwidget.desktop
