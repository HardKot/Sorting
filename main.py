import os
from listtype import types

def bisearch(arr, name):
    middle = len(arr) // 2
    if arr[middle] == name:
        return True
    if len(arr) == 1:
        return False
    if name < arr[middle]:
        return bisearch(arr[:middle], name)
    if name > arr[middle]:
        return bisearch(arr[middle:], name)

def typewriter(format):
    for type in types:
        if bisearch(types.get(type), format):
            return type
    else:
        return False

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
        type = typewriter(format)
        if type:
            os.system(r'move "{0}\{1}" c:\users\{2}\{3}'.format(os.getcwd(),
                                                                file,
                                                                os.getlogin(),
                                                                type))

scaning()
