#!/usr/bin/env python3

from os import path, getenv, system
import sys
import ttkbootstrap as tkb
from ttkbootstrap import BOTH, RIGHT, Toplevel, SUNKEN, Text, Scrollbar,Label, Entry, Meter
from PIL import Image, ImageTk
from libs import keys_actions
from libs import read_write
from libs import file_from_args
from libs import counter
from tkterminal import Terminal 


help_contents = '''

INSERT MODE : <F1>
SAVE   MODE : <F2>
OPEN   MODE : <F3>
HELP   MODE : <F4>
TERMINAL    : <F5>
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
    #icon loader
    theme_selected_latest = ''
    with open('theme.conf', 'r') as theme_selected:
        theme_selected_latest = theme_selected.read()
        print(theme_selected_latest)




    master = tkb.Window(
        themename='%s' % theme_selected_latest.split('\n')[14].replace('theme=', '').strip(), 
        title="LuxarG",


    )
        
    if sys.platform == 'linux' or sys.platform == 'linux2':
        master.iconbitmap('/usr/share/icons/luxarg.png')
        
    elif sys.platform == 'win32':
        master.iconbitmap('./luxarg.ico')



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

    show_font_size = Label(bootstyle='info', font=font_size)
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
    def run_terminal():

        terminal_bar = Toplevel(master)
        terminal_bar.title('Luxarg Terminal')
        terminal = Terminal(terminal_bar, pady=10, padx=10)
        terminal.shell = True
        
        terminal.config(
    insertborderwidth=1,
    insertwidth=5,
    width=30,
    padx=20,
    pady=4,
    font=('', font_size))
        terminal.focus()
        terminal.pack(expand=True, fill='both')

    
    
    # TODO : terminal emulator MUST be develop here
       # HELP MODE (binding F5)

    text_field.bind('<F5>', lambda e :run_terminal())

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
