#!/usr/bin/env python3

from ttkbootstrap import Toplevel, Label
from libs import read_write

########-#######################################################
# file_mode = '\nExample : /tmp/tmp\n<ESC> for exit'
file_mode = ''

###############################################################
def insert_mode(text_field, show_status, status ):
    '''insert mode'''
    show_status.config(bootstyle='success')
    # show insert mode status
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status

    #return all
    return text_field.configure(state='normal'), show_status

###############################################################
def stop_mode(text_field, show_status, status ):
    ''' stop mode '''
    # show stop mode status
    show_status.config(bootstyle=' danger')

    show_status['text'] = '%s\nHELP MODE : <F4> ' % status


    # return all
    return text_field.configure(state='disabled'), show_status


###############################################################
def save_mode(text_field, show_status, status, save_path):
    ''' save mode '''
    show_status.config(bootstyle=' info')
    save_path.focus()
    save_path.select_range(0, 'end')

    # save file with ENTER
    save_path.bind('<Return>', lambda e :
        read_write.io_luxarg(save_path.get().strip(),
        text_field.get('1.0', 'end').strip(),
        'w',
        text_field
        )

    )

    # go to stop mode
    show_status['text'] = '%s\nHELP MODE : <F4>%s' % (status, file_mode)

    # if the user want to leave file Entry
    save_path.bind('<Escape>', lambda e : text_field.focus())

    # return all
    return text_field.configure(state='disabled'), show_status

###############################################################
def open_mode(text_field, show_status, status, file_path):
    ''' open mode '''
    show_status.config(bootstyle='warning')

    file_path.focus()
    file_path.select_range(0, 'end')

    # open file with ENTER
    file_path.bind('<Return>',
        lambda e :
        read_write.io_luxarg(
            file_path.get().strip(),
            None,
            'r',
            text_field
        )
    )

    # show open mode status

    show_status['text'] = '%s\nHELP MODE : <F4>%s' % (status, file_mode)
    show_status.config(bootstyle='warning')
    file_path.bind('<Escape>', lambda e : text_field.focus())

    # return all
    return text_field.configure(state='normal'), show_status


###############################################################
def help_mode(master, show_status, status, help_contents):
    ''' help mode '''
    help_window=Toplevel(master)
    help_window.title(' LUXARG :: HELP ')
    help_window.maxsize()


    help_label = Label(help_window, text=help_contents, font=('', 15))
    # help_label.config(background=bg_fg_color.bg, foreground=bg_fg_color.fg) #DEPRICATED
    #Help content bootstrap color scheme
    help_label.config(bootstyle='light', padding=10)
    help_label.pack()
    show_status['text'] = '%s\nHELP MODE : <F4> ' % status
    show_status.config(bootstyle='primary')
    return show_status