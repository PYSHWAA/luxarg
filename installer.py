#!/usr/bin/env python3 
''' 

AMZY-0 (M.Amin Azimi .K) 
Copyright (C) (2019-2020-2021)  AMZY-0 (M.Amin Azimi .K) 

"Luxarg" (This program) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''

from os import system, getenv
system('sudo pip install -r requirements.txt')

# quit from installed message
def quit(key):
    if key in 'q':
        raise urwid.ExitMainLoop()
# home address (~)  
HOME_ADDR = getenv('HOME')

if  system('''
        sudo apt install python3-tk -y  2> /dev/null;
        sudo dnf install -y python3-tkinter 2> /dev/null;
        sudo pacman -S tk -y 2> /dev/null;
        sudo yum install -y python3-tkinter  2> /dev/null;
        sudo zypper in -y python-tk 2> /dev/null;
            ''')==0:
            pass
elif (system('''
        pip3 install --upgrade pip;
        pip3 install virtualenv;
        virtualenv venv;
        source venv/bin/activate;
        pip3 install -r requirements.txt;
        mkdir ~/.luxarg ; sudo mkdir /root/.luxarg;
        cp -rf .  ~/.luxarg/;
        sudo cp -rf .  /root/.luxarg/;
        sudo rm /usr/bin/luxarg 2> /dev/null; 
        sudo unlink /usr/bin/luxarg-update 2> /dev/null;
        pyinstaller -w -F --name 'luxarg'  --hidden-import='PIL._tkinter_finder' -i "./icon/luxarg.png"  core.py;
        cp ./dist/luxarg . ;
        rm -rf __pycache__/ build/ core.spec dist/ luxarg.spec ;
        sudo cp luxarg /usr/bin;
        sudo cp %s/.luxarg/luxarg /usr/bin/ ;
        sudo ln -s %s/.luxarg/update.py /usr/bin/luxarg-update;''' 
    % (HOME_ADDR, HOME_ADDR))) == 0:
 
    # install dependencies
    
    # desktop application icon for menu 
    system('sudo cp -rf ./xdg/luxarg.desktop /usr/share/applications')
    system('cp -rf ./xdg/luxarg.desktop ~/.local/share/applications')
    system("sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/")
    system("sudo cp -rf ./icon/luxarg.png /usr/share/icons/hicolor/256x256/apps/")
    system("sudo cp -rf ./icon/luxarg.png /usr/share/icons/")

    # installed successfuly message
    import urwid
    txt = urwid.Text(u'Luxarg INSTALLED successfuly !\nfor quit : \'q\'', align='left')
    fill = urwid.Filler(txt, 'middle')
    loop = urwid.MainLoop(fill, unhandled_input=quit)
    loop.run()
    system('exec %s && exit' %getenv('SHELL'))
 
else:
    print('status : broken !')

