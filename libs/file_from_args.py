#!/usr/bin/env python3


def open_mode_by_arg(text_field, show_status, io_mode, path_arg):
    '''$ luxarg file_path/filename.txt'''
    text_field.configure(stat='normal')

    # open file with read mode
    fin = open(path_arg, io_mode)

    #insert from file
    text_field.delete('1.0', 'end')
    text_field.insert('1.0', fin.read())

    #change status
    show_status['text']='✒OPEN_MODE✒\nHELP MODE : <F4>'
    show_status.config(bootstyle='warning')
    text_field.configure(state='disabled')

    # close the file
    fin.close()
