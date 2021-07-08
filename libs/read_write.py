#!/usr/bin/python3

''' 


Copyright [2019-2020-2021] [M.Amin Azimi .K (amzy-0)]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

'''

from tkinter import messagebox
from os import path
from os import getenv


def message(path_msg, text_msg):


    if text_msg == 'saved !':
        msg = messagebox.showinfo('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))
    
    else:
        msg = messagebox.showerror('%s'%text_msg, 
        message='%s  %s' % (path_msg, text_msg))


def writer(path_and_filename, text, widget_destroy):
    
    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = '''Field is empty !
Please HIT <F2> and enter your file name again ...'''
        message(path_and_filename, '')

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory')   

    elif path_and_filename[:2] == '~/':
        path_and_filename = path_and_filename.replace('~/','%s/'% 
        str(getenv('HOME'))).strip()
    
        try:
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    

    # relational path for home
    elif path_and_filename[:2] == '~/':
        path_and_filename = path_and_filename.replace('~/','%s/'% 
        str(getenv('HOME'))).strip()
        
        try:
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    
    # relational path for home directory added (~)  
    elif path_and_filename == '~':
            message(path_and_filename, ': Is directory')

    else:
        
        try:
            fin = open(path_and_filename, 'w')
            fin.write(text)
            message(path_and_filename, 'saved !')
            
            fin.close()
        
        except OSError as error :
            message(path_and_filename, str(error)[10:])
    

    return widget_destroy.destroy()



# read a file 
def reader(path_and_filename, text_field, widget_destroy=None):

    # delete all the buffer and after open file 
    text_field.delete('1.0', 'end')
    # path_and_filename equal to EMPTY 
    if path_and_filename == '':
        path_and_filename = 'Field is empty !\nPlease HIT <F2> and enter your path and file name again ...'
        message(path_and_filename, '')
        

    # if is directory :
    elif path.isdir(path_and_filename) or path_and_filename[-1] == '/':
        # if not a file 
        message(path_and_filename, ': Is directory (Directory is not readable)')   
        

    # if a file 
    else:
        try:

            fin = open(path_and_filename, 'r')
            readed =  fin.read()

        
        except OSError as error:
            message('', str(error)[10:])
   
        fin.close()
        
    try:    
        text_field.insert('1.0', str(readed))
        text_field.configure(state='disabled')
        
    
    except:
        text_field.configure(state='disabled')
        
    return widget_destroy.destroy()

