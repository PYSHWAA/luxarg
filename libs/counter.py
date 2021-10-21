# line number 
def linenum(text_field, showline_stat):

    chars = len(text_field.get('1.0', 'end'))-1
    showline_stat['text'] = '%s char(s) | ' % chars

    lines = len(text_field.get('1.0', 'end').split('\n'))-1
    showline_stat['text'] += '%s line(s)' % lines 