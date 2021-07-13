def open_mode_inside(text_field, show_status, io_mode, path_arg):

    text_field.configure(stat='normal')
    
    # open file with read mode 
    fin = open(path_arg, io_mode)
    
    #insert from file 
    text_field.delete('1.0', 'end')
    text_field.insert('1.0', fin.read())
    
    #change status
    show_status['text']='__OPEN_MODE__\nSAVE MODE : <F2>'
    text_field.configure(state='disabled')

    # close the file 
    fin.close()