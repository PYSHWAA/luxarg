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

update:
	@sudo git reset FETCH_HEAD;sudo git restore . ;sudo git pull

install:
	-@sudo rm -rf ~/.luxarg /usr/share/luxarg /opt/luxarg/*

	-@sudo apt install python3-tk -y  2> /dev/null || true
	
	-@sudo dnf install -y python3-tkinter 2> /dev/null || true
	
	-@sudo pacman -Syu tk --noconfirm 2> /dev/null || true
	
	-@sudo yum install -y python3-tkinter 2> /dev/null || true
	
	-@sudo zypper in -y python-tk 2> /dev/null || true

	-@pip3 install -U pip
		
	-@pip3 install -r requirements.txt 
		
	-@sudo mkdir -p /opt/luxarg

	-@sudo cp -rf . ./.git ./.gitignore /opt/luxarg
		
	-@sudo rm -f /usr/bin/luxarg 
		
	-@sudo unlink /usr/bin/luxarg-update 2> /dev/null;
    
	-@sudo cp -rf ./xdg/luxarg.desktop /usr/share/applications
    
	-@cp -rf ./xdg/luxarg.desktop ~/.local/share/applications
    
	-@sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/
    
	-@sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/
    
	-@sudo cp -rf ./icon/luxarg.png /usr/share/icons/
		
	-@echo "exec /opt/luxarg/core.py \$$1" > luxarg 
	
	@sudo chmod 755 luxarg
	
	-@sudo cp luxarg /usr/bin/
	-@sudo rm ./luxarg
	-@sudo ln -s /opt/luxarg/update.py /usr/bin/luxarg-update
