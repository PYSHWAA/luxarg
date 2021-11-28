# AMZY-0 (M.Amin Azimi .K) 
# Copyright (C) 2019-2021 luxarg AMZY-0 (M.Amin Azimi .K) and contributors
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


clean: 
	-@rm -rf __pycache__/ build/ core.spec dist/ luxarg.spec 


install: local

	-@mkdir ~/.luxarg || true
	
	-@cp -rf .  ~/.luxarg/
	
	@pyinstaller -w --onedir  --name 'luxarg'  --hidden-import='PIL._tkinter_finder' -i "./icon/luxarg.png"  core.py

	-@mv ./dist/luxarg . || true
	
	-@sudo rm -f /usr/bin/luxarg 
	
	-@sudo rm -rf /usr/share/luxarg
	
	-@sudo unlink /usr/bin/luxarg-update 2> /dev/null;
    
	-@sudo cp -rf ./xdg/luxarg.desktop /usr/share/applications
    
	-@cp -rf ./xdg/luxarg.desktop ~/.local/share/applications
    
	-@sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/
    
	-@sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/
    
	-@sudo cp -rf ./icon/luxarg.png /usr/share/icons/
	
	-@sudo cp -rf luxarg/ /usr/share && rm -rf luxarg/
	
	-@echo "exec /usr/share/luxarg/luxarg \$$1" > luxarg 
	
	@sudo chmod 755 luxarg
	
	-@sudo cp luxarg /usr/bin/
	
	-@sudo ln -s ~/.luxarg/update.py /usr/bin/luxarg-update
	
	@rm luxarg

local:

	-@sudo apt install python3-tk -y  2> /dev/null || true
	
	-@sudo dnf install -y python3-tkinter 2> /dev/null || true
	
	-@sudo pacman -S tk -y 2> /dev/null || true
	
	-@sudo yum install -y python3-tkinter 2> /dev/null || true
	
	-@sudo zypper in -y python-tk 2> /dev/null || true

	-@pip3 install --upgrade pip
	
	-@sudo pip3 install virtualenv
	
	-@sudo pip3 install pyinstaller
	
	@rm -rf venv luxarg
	
	@virtualenv venv
	
	. ./venv/bin/activate;
	
	-@ pip install -Ur requirements.txt
	