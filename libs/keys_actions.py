#!/usr/bin/python3

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

from tkinter import BOTH, Toplevel, Label
from . import read_write

global file_mode 
file_mode = '\nExample : /tmp/tmp\n<ESC> for exit'

# insert mode 
def insert_mode(text_field, show_status, status ):
    # show insert mode status
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status
    
    #return all 
    return text_field.configure(state='normal'), show_status


# stop mode 
def stop_mode(text_field, show_status, status ):
    
    # show stop mode status

    show_status['text'] = '%s\nHELP MODE : <F4> ' % status


    # return all 
    return text_field.configure(state='disabled'), show_status


# save mode 
def save_mode(text_field, show_status, status, save_path):

    save_path.focus()
    save_path.select_range(0, 'end')
    
    # save file with ENTER
    save_path.bind('<Return>', lambda e : 
        read_write.io_luxarg(save_path.get().strip(),
        text_field.get('1.0', 'end').strip(),
        'w',
        text_field,
        save_path
        )
        
    )

    # go to stop mode 
    show_status['text'] = '%s\nHELP MODE : <F4>%s' % (status, file_mode)

    # if the user want to leave file Entry
    save_path.bind('<Escape>', lambda e : text_field.focus())

    # return all 
    return text_field.configure(state='disabled'), show_status 


#open mode 
def open_mode(text_field, show_status, status, file_path):
    
    file_path.focus()
    file_path.select_range(0, 'end')

    # open file with ENTER
    file_path.bind('<Return>', 
        lambda e : 
        read_write.io_luxarg(
            file_path.get().strip(), 
            None,
            'r', 
            text_field,
            file_path
        )
    )
    
    # show open mode status
    show_status['text'] = '%s\nHELP MODE : <F4>%s' % (status, file_mode)

    file_path.bind('<Escape>', lambda e : text_field.focus())
    
    # return all
    return text_field.configure(state='normal'), show_status



#help mode
def help_mode(master, show_status, status, help_contents):
    help_window=Toplevel(master)
    help_window.title(' LUXARG => HELP ')
    help_window.maxsize()
    

    help_label = Label(help_window, text=help_contents, font=('', 17))
    help_window.config(bg='black')
    help_label.config(background='black', foreground='white')
    help_label.pack()
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status
    return show_status
