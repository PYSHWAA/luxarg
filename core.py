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

from os import getenv
from sys import argv, exit
from tkinter import BOTH, RIGHT, SUNKEN, Tk, Text, Scrollbar,Label, Entry
from libs.keys_actions import *
from PIL import Image, ImageTk
from libs.read_write import message
from libs.file_from_args import open_mode_by_arg

help_contents = '''

INSERT MODE : <F1>
SAVE   MODE : <F2>
OPEN   MODE : <F3>
HELP   MODE : <F4>
DELETE ALL  : <Ctrl + 0>
SELECT ALL  : <Ctrl + />
CORSUR RIGHT: <Ctrl + f> move the cursor forward one space.
CORSUR LEFT : <Ctrl + b> move the cursor backward one space.
Copy        : <Ctrl + c>
Paste       : <Ctrl + v>
Cut         : <Ctrl + w>
UNDO        : <Ctrl + z>
REDO        : <Ctrl + Shift + z>
HELP   CLI  : luxarg <-h/--help>
ZOOM IN     : <Ctrl + equal(+)>
ZOOM OUT    : <Ctrl + minus(-)>
    
'''

master = Tk()
master.geometry("700x700")
master.title("LuxarG")
master.minsize(height=500, width=500)
master.config(bg='black')

show_status = Label() 
show_status['text']='__STOP_MODE__\nHELP MODE : <F4>'
show_status['bg']='black'
show_status['fg']='white'
show_status['font']=('sans', 13)

show_status.pack(fill='x')

# for storing all the file_path variable value
file_path = Entry(master, font=('', 13))

# "file_path" configure : 
file_path.configure(bg='black', 
    fg='white',
    insertbackground='yellow',
)

file_path.insert(0, 'file path example : /tmp/tmp')
file_path.pack(fill=BOTH)

# adding scrollbar
scrollbar = Scrollbar(master)

# packing scrollbar
scrollbar.pack(side=RIGHT, fill='y')

# definition a text_field 
text_field = Text(master, yscrollcommand=scrollbar.set, undo=True)
text_field.pack(expand=True, fill=BOTH)
text_field.configure(spacing2=130)
text_field.focus()
# text_field.columnconfigure(0, pad=10)

if argv[0] and len(argv) ==1:
    pass
elif argv[1] == '-h' or argv[1]=='--help':
    print(help_contents)

    master.forget(master)
    exit()

try:
    #try to set logo 
    img = ImageTk.PhotoImage(Image.open('%s/.luxarg/icon/luxarg.png' % getenv('HOME')))
    master.iconphoto(False, img)

# if logo not found, just continue 
except:
    pass

# set font size to 20
font_size = 20

#font resizer 
def font_resizer(component, minesOrPlus):
    global font_size 
    
  
    if minesOrPlus == '+' and font_size <= 100: 
        component['font'] = ('', font_size + 1)
        font_size += 1
    elif minesOrPlus == '-' and font_size >= 10 : 
        component['font'] = ('', font_size - 1)
        font_size -= 1

        return component['font']
    
    else:
        return




# INSERT MODE (binding F1)
text_field.bind('<F1>', lambda e :  insert_mode(
    text_field,
    show_status,
    '__INSERT_MODE__'
    )
)
# STOP MODE (binding ESC)
text_field.bind('<Escape>', lambda e :  stop_mode(
    text_field,
    show_status,
    '__STOP_MODE__'
    )
)

# SAVE MODE (binding F2)
text_field.bind('<F2>', lambda e :  save_mode(
    text_field,
    show_status,
    '__SAVE_MODE__',
    file_path
    )
)

# OPEN MODE (binding F3)
text_field.bind('<F3>', lambda e: open_mode(
    text_field,
    show_status,
    '__OPEN_MODE__',
    file_path
    )
)

# HELP MODE (binding F4)
text_field.bind('<F4>', lambda e: help_mode(
    master,
    show_status,
    '__HELP_MODE__',
    help_contents
    )
)

# UNDO
text_field.bind('<Control-Z>', lambda e : text_field.edit_undo)

# REDO
text_field.bind('<Control-Shift-Z>', lambda e : text_field.edit_redo)

# zoom control by CTRL + Mouse scroll 
# text_field.bind('<Control-Button-4>', lambda e : font_resizer(text_field, '+'))
# text_field.bind('<Control-Button-5>', lambda e : font_resizer(text_field, '-'))
text_field.bind('<Control-equal>', lambda e : font_resizer(text_field, '+'))
text_field.bind('<Control-minus>', lambda e : font_resizer(text_field, '-'))

# delete all with CTRL + 0
text_field.bind('<Control-0>', lambda e :text_field.delete('1.0', 'end'))

# ENTER from keypad 
text_field.bind('<KP_Enter>', lambda e : text_field.insert('end', '\n'))

try:
    # try open file from the arg1 (like this : $ luxarg /tmp/tmp)
    try:
        open_mode_by_arg(text_field, show_status, 'r', argv[1])
        
    # if pass is not true 
    except OSError as error:
        
        message('', str(error)[10:])
except:
    pass

# DISABLE text box 
text_field.configure(state='disabled')

text_field.config(bg='black', fg='white', 
                padx=15, pady=0, 
                relief=SUNKEN, 
                insertbackground='yellow', insertborderwidth=1,
                font=('', font_size)
                )


# text_field
# configuring the scrollbar
scrollbar.config(bg='gray', command=text_field.yview)


master.mainloop()
