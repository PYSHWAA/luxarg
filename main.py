#!/usr/bin/env python3

'''
AMZYEI (M.Amin Azimi .K)
Copyright (C) 2019-2021 luxarg AMZYEI (M.Amin Azimi .K) and contributors

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
from os import path, getenv
import sys
import ttkbootstrap as tkb
from ttkbootstrap import BOTH, RIGHT, LEFT, SUNKEN, Text, Scrollbar,Label, Entry, Meter
from PIL import Image, ImageTk
from libs import keys_actions
from libs import read_write
from libs import file_from_args
from libs import counter
from libs import theme

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
ZOOM IN     : <Ctrl + equal(=)>
ZOOM OUT    : <Ctrl + minus(-)>

* For exit from other modes(INSERT/OPEN/SAVE), please hit ESC! *

'''



def main():
    ''' The Main function (entry point) '''
    master = tkb.Window(themename=theme.theme, 
    title="LuxarG",
    iconphoto = '/usr/share/icons/luxarg.png'
    )



    master.geometry("700x700")
    master.title("LuxarG")
    master.minsize(height=500, width=500)
    # master.config(bg=bg_fg_color.bg)

    show_status = Label(master, bootstyle='danger')
    show_status['text'] = '😈STOP_MODE😈\nHELP MODE : <F4>'

    show_status['font'] = ('', 14)

    #for line status
    showline_stat = Label(master, bootstyle='info')
    # showline_stat['bg']=bg_fg_color.bg
    # showline_stat['fg']=bg_fg_color.fg
    showline_stat['font']  = ('', 14)


# load statusbar before all components          
    showline_stat.pack(fill=BOTH)
    show_status.pack(fill='y')

    # for storing all the file_path variable value
    # global file_path

    file_path = Entry(master, font=('', 14), bootstyle='primary')

    # "file_path" configure :
    # file_path.configure(
    #     insertbackground='yellow'
    # ) ## OLD VERSION 1.0

    file_path.insert(0, 'file path example : /tmp/tmp')
    file_path.pack(fill=BOTH)

    # adding scrollbar
    scrollbar = Scrollbar(master, bootstyle='info')

    # packing scrollbar
    scrollbar.pack(side=RIGHT, fill='y')

    # definition a text_field
    text_field = Text(master, yscrollcommand=scrollbar.set, undo=True)
    text_field.pack(expand=True, fill=BOTH)
    text_field.focus()


    if sys.argv[0] and len(sys.argv) ==1:
        pass
    elif sys.argv[1] in ['-h', '--help']:
        print(help_contents)

        master.forget(master)
        sys.exit()


    # set font size to 20
    global font_size
    font_size = 20


    def font_resizer(component, mines_or_plus):
        '''font resizer'''

        global font_size

        if mines_or_plus == '+' and font_size <= 100:
            component['font'] = ('', font_size + 1)
            font_size += 1
        elif mines_or_plus == '-' and font_size >= 10 :
            component['font'] = ('', font_size - 1)
            font_size -= 1

        return component['font']

    show_font_size = Meter(bootstyle='info', metersize=font_size)
    show_font_size.pack()


    #####################################################
    #                                                   #
    #                  key binding                      #
    #                                                   #
    #####################################################



    # INSERT MODE (binding F1)
    text_field.bind('<F1>', lambda e :  keys_actions.insert_mode(
        text_field,
        show_status,
        '✍INSERT_MODE✍'
        ))

    # STOP MODE (binding ESC)
    text_field.bind('<Escape>', lambda e :  keys_actions.stop_mode(
        text_field,
        show_status,
        '😈STOP_MODE😈'
        )
    )

    # SAVE MODE (binding F2)
    text_field.bind('<F2>', lambda e :  keys_actions.save_mode(
        text_field,
        show_status,
        '♨SAVE_MODE♨',
        file_path,
        )
    )

    # OPEN MODE (binding F3)
    text_field.bind('<F3>', lambda e: keys_actions.open_mode(
        text_field,
        show_status,
        '✒OPEN_MODE✒',
        file_path
        )
    )

    # HELP MODE (binding F4)
    text_field.bind('<F4>', lambda e: keys_actions.help_mode(
        master,
        show_status,
        '☠ HELP_MODE ☠',
        help_contents
        )
    )

    # UNDO
    text_field.bind('<Control-Z>', lambda e : text_field.edit_undo)

    # REDO
    text_field.bind('<Control-Shift-Z>', lambda e : text_field.edit_redo)

    # zoom control by CTRL + Mouse scroll
    # text_field.bind('<Control-Button-4>', 
    # lambda e : font_resizer(text_field, '+'))
    # text_field.bind('<Control-Button-5>', 
    # lambda e : font_resizer(text_field, '-'))
    text_field.bind('<Control-equal>', 
    lambda e : font_resizer(text_field, '+'))
    text_field.bind('<Control-minus>', 
    lambda e : font_resizer(text_field, '-'))

    # delete all with CTRL + 0
    text_field.bind('<Control-0>', 
    lambda e :text_field.delete('1.0', 'end'))
    

    # key binding for calc lines
    text_field.bind('<BackSpace>', 
    lambda e: counter.linenum(text_field, showline_stat))
    text_field.bind('<Return>', 
    lambda e : counter.linenum(text_field, showline_stat))
    text_field.bind('<KP_Enter>', 
    lambda e : text_field.insert('end', '\n'),
    counter.linenum(text_field, 
    showline_stat))
    text_field.bind('<KeyRelease>', 
    lambda e: counter.linenum(text_field, showline_stat))


    try:
        # try open file from the arg1 (like this : $ luxarg /tmp/tmp)
        try:
            file_from_args.open_mode_by_arg(
                text_field, 
                show_status, 
                'r',
                sys.argv[1]
                )
            
            file_path.delete(0, 'end')
            file_path.insert(0, str(path.expanduser(sys.argv[1])))
            
            counter.linenum(text_field, showline_stat)
        
        # if pass is not true
        except OSError as error:
            read_write.message('', str(error)[10:])
            text_field.focus()
    except:
        pass

    # DISABLE text box
    text_field.configure(state='disabled')

    # tab setting

    # text field configuration

    text_field.config(
    relief=SUNKEN,
    spacing1=10,
    insertborderwidth=1,
    insertwidth=5,
    width=20,
    padx=20,
    pady=4,
    font=('', font_size),
    
    )


    # configuring the scrollbar
    scrollbar.config(bootstyle='secondary', command=text_field.yview)

    master.mainloop()


if __name__ == '__main__':
    main()
