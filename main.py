import os
import formats

def scaning():
    files = list(filter(os.path.isfile, os.listdir()))
    for file in files:
        format = ''
        for i in range(len(file) - 1, 0, -1):
            if file[i] == '.':
                break
            format += file[i]
        else:
            continue
        format = format[::-1]
        type = formats.searchtype(format)
        if type:
            os.system(r'move "{0}\{1}" c:\users\{2}\{3}'.format(os.getcwd(),
                                                                file,
                                                                os.getlogin(),
                                                                type))

    
