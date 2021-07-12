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

from os import system, chdir, getenv
print('...')
chdir('%s/.luxarg/' % getenv('HOME')) 

system('git reset FETCH_HEAD; git restore . ; git pull')

system('sudo rm -f /usr/bin/luxarg')
system('rm -f ./luxarg; ./installer.py')
system('sudo cp -f luxarg /usr/bin/')
system('rm luxarg')
print('...')




