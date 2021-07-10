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
from tkinter import BOTH, RIGHT, SUNKEN, Tk, Text, Scrollbar,Label
from libs.keys_actions import *
from PIL import Image, ImageTk

help_contents = '''

INSERT MODE : <F1>
SAVE   MODE : <F2>
OPEN   MODE : <F3>
HELP   MODE : <F4>
DELETE ALL  : <Ctrl + 0>
SELECT ALL  : <Ctrl + />
CORSUR RIGHT: <Ctrl + f> The CURSOR move the cursor forward one space.
CORSUR LEFT : <Ctrl + b> The CURSOR move the cursor backward one space.
Copy        : <Ctrl + c>
Paste       : <Ctrl + v>
Cut         : <Ctrl + w>
HELP   CLI  : luxarg <-h/--help>
ZOOM IN     : <Ctrl + sroll UP>
ZOOM OUT    : <Ctrl + sroll Down>

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
show_status['font']=('', 13)

show_status.pack(fill='x')

# adding scrollbar
scrollbar = Scrollbar(master)

# packing scrollbar
scrollbar.pack(side=RIGHT, fill='y')

# definition a text_field 
text_field = Text(master, yscrollcommand=scrollbar.set, undo=True)
text_field.pack(expand=True, fill=BOTH)
text_field.focus()


if argv[0] and len(argv) ==1:
    pass
elif argv[1] == '-h' or argv[1]=='--help':
    print(help_contents)

    master.forget(master)
    exit()
 
      

# try:
    # try to set logo 
img = ImageTk.PhotoImage(Image.open('%s/.luxarg/icon/luxarg.png' % getenv('HOME')))
master.iconphoto(False, img)

# except:
#    pass

# set font size to 20
font_size = 20

#font resizer 
def font_resizer(component, minesOrPlus):
    global font_size 
    if minesOrPlus == '+': 
        component['font'] = ('', font_size + 1)
        font_size += 1
    else: 
        component['font'] = ('', font_size - 1)
        font_size -= 1
    
    return component['font']




# INSERT MODE (binding F1)
text_field.bind('<F1>', lambda e :  insert_mode(text_field, show_status, '__INSERT_MODE__'))

# STOP MODE (binding ESC)
text_field.bind('<Escape>', lambda e :  stop_mode(text_field, show_status, '__STOP_MODE__'))

# SAVE MODE (binding F2)
text_field.bind('<F2>', lambda e :  save_mode(master, text_field, show_status, '__SAVE_MODE__'))

# OPEN MODE (binding F3)
text_field.bind('<F3>', lambda e: open_mode(master, text_field, show_status, '__OPEN_MODE__'))

# HELP MODE (binding F4)
text_field.bind('<F4>', lambda e: help_mode(master, show_status, '__HELP_MODE__', help_contents))

# UNDO
text_field.bind('<Control-Z>', lambda e : text_field.edit_undo)
# REDO
text_field.bind('<Control-R>', lambda e : text_field.edit_redo)

# zoom control by CTRL + Mouse scroll 
text_field.bind('<Control-Button-4>', lambda e : font_resizer(text_field, '+'))
text_field.bind('<Control-Button-5>', lambda e : font_resizer(text_field, '-'))

# delete all with CTRL + 0
text_field.bind('<Control-0>', lambda e :text_field.delete('1.0', 'end'))

# ENTER from keypad 
text_field.bind('<KP_Enter>', lambda e : text_field.insert('end', '\n'))

try:
    # try open file from the arg1 (like this : $ luxarg /tmp/tmp)
    try:
        text_field.configure(stat='normal')
        fin = open(argv[1], 'r')
        text_field.delete('1.0', 'end')
        text_field.insert('1.0', fin.read())
        show_status['text']='__OPEN_MODE__\nSAVE MODE : <F4>'
        text_field.configure(state='disabled')

        fin.close()

    # if pass is not true 
    except OSError as error:
        from libs.read_write import message
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
