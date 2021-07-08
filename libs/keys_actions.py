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


from tkinter import BOTH, Toplevel, Entry, Label
from tkinter.messagebox import showerror  
from . import read_write

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
def save_mode(master, text_field, show_status, status ):
    
    # save mode box for user input 
    save_mode_window = Toplevel(master)
    save_mode_window.title('PATH and FILE NAME (SAVE):')
    save_mode_window.resizable(False, False)
    save_mode_window.geometry('500x25')
    
    # show stop mode status
    show_status['text'] = '%s\nSAVE path example : /tmp/file_name.txt' % status
    
    # for storing all the save_path variable value
    save_path = Entry(save_mode_window, font=('', 13))
    save_path.config(bg='black', fg='white', insertbackground='yellow')
    save_path.focus()
    save_path.pack(fill=BOTH)

    # save file with ENTER
    save_path.bind('<Return>', lambda e : 
        read_write.writer(save_path.get().strip(),
        text_field.get('1.0', 'end').strip(),
        save_mode_window)
    )

    # go to stop mode 
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status
    # return all 
    return text_field.configure(state='disabled'), show_status


#open mode 
def open_mode(master, text_field, show_status, status):


    open_file_window = Toplevel(master)
    open_file_window.title(' PATH and FILE NAME (OPEN):')
    open_file_window.resizable(False, False)
    open_file_window.geometry('450x25')
    
    # for storing all the file_path variable value
    file_path = Entry(open_file_window, font=('', 13))
    file_path.config(bg='black', fg='white', insertbackground='yellow')
    file_path.pack(fill=BOTH)
    file_path.focus()
    
    # open file with ENTER
    file_path.bind('<Return>', 
        lambda e : read_write.reader(file_path.get().strip(), text_field, open_file_window)
    )
    
    # show open mode status
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status

    # return all
    return show_status, text_field.configure(state='normal')



#help mode
def help_mode(master, show_status, status, help_contents):
    help_window=Toplevel(master)
    help_window.title(' LUXARG => HELP ')
    help_window.geometry('430x350')
    

    help_label = Label(help_window, text=help_contents, font=('', 17))
    help_window.config(bg='black')
    help_label.config(background='black', foreground='white')
    help_label.pack()
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status
    return show_status
