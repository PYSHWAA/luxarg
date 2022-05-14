#!/usr/bin/env python3

'''
AMZY-0 (M.Amin Azimi .K)
Copyright (C) 2019-2021 luxarg AMZY-0 (M.Amin Azimi .K) and contributors

Luxarg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Luxarg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
This file is part of Luxarg.
Luxarg is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Luxarg is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License

'''

from os import system, chdir

print('...')

if (system('ping -c2 4.2.2.4 > /dev/null 2>&1')) == 0 :

    chdir('/tmp/')
    system('pwd')
    system('sudo rm -rf /opt/luxarg')
    system('git clone https://github.com/amzy-0/luxarg')
    chdir('luxarg')
    system('make install')
    system('rm -rf /tmp/luxarg')
else: 
    print(u'\U00002195', 'internet connection error!'.capitalize(), u'\U00002195')

print('...')
