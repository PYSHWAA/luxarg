# AMZYEI (M.Amin Azimi .K) 
# Copyright (C) 2019-2021 luxarg AMZYEI (M.Amin Azimi .K) and contributors
# 
# Luxarg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Luxarg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# This file is part of Luxarg.
#
# Luxarg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Luxarg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License


SHELL = bash

.DEFAULT_GOAL := install

install:
	-@sudo rm -rf ~/.luxarg /usr/share/luxarg /bin/*luxarg*
	-@sudo unlink /bin/luxarg /bin/luxarg-update 2> /dev/null/ ;

	-@sudo apt install python3-tk -y  2> /dev/null || true
	
	-@sudo dnf install -y python3-tkinter 2> /dev/null || true
	
	-@sudo pacman -Syu tk --noconfirm 2> /dev/null || true
	
	-@sudo yum install -y python3-tkinter 2> /dev/null || true
	
	-@sudo zypper in -y python-tk 2> /dev/null || true

	-@pip3 install -U pip
		
	-@pip3 install -Ur requirements.txt
	
	-@sudo pip3 install -Ur requirements.txt

	-@sudo mkdir -p /opt/luxarg 2> /dev/null 

	-@sudo cp -rf . .*git* /opt/luxarg 2> /dev/null
    
	-@sudo cp -rf `pwd`/xdg/luxarg.desktop /usr/share/applications
    
	-@cp -rf `pwd`/xdg/luxarg.desktop ~/.local/share/applications
    
	-@sudo cp -rf `pwd`/icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/
    
	-@sudo cp -rf `pwd`/icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/
    
	-@sudo cp -rf `pwd`/icon/luxarg.png /usr/share/icons/
	
	-@sudo ln -s /opt/luxarg/update.py /usr/bin/luxarg-update
	
	-@sudo ln -s /opt/luxarg/main.py /usr/bin/luxarg		
	
